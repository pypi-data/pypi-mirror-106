try:
    import unzip_requirements
except ImportError:
    pass
import hszinc#.zincparser
import copy
import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import DynamicImporter as dy
import GetPredictionIntervals as pi
import StoreRetrieveModel as srm
import config as cfg
import pandas as pd
import json
import logging
import gc
from rq import get_current_job


isaws = cfg.environment["isaws"]
PROJECT_PATH = ""
root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO)


def create_features(contents):
    global PROJECT_PATH
    # Pre-process training data
    #contents = event["body"]
    #contents = ''.join(x for x in contents if ord(x) < 128)
    import json
    grids = hszinc.parse(contents, mode=hszinc.MODE_JSON) # Get Meta from Json data
    g = grids
    df = pd.DataFrame.from_records(grids)  # convert JSON to dataframe
    # Call problem statement specific create feature function
    di = dy.DynamicImporter("src.probStatements."+g.metadata["problemStatement"].replace(" ", ""), "create_features")
    create_features = di.get_class()
    data, target = create_features(df, grids.metadata["data"])
    return data, target, g.metadata


def put_data_redis_cache(hash_name,hash_key,hash_data):
    import redis
    from datetime import datetime, timedelta
    r = redis.from_url(url="redis://redis:6379/0")#redis.Redis(host=os.environ["REDIS_HOST"], port=os.environ["REDIS_PORT"])
    ttl = int(timedelta(hours=8).total_seconds())
    r.hset(name=hash_name, key=hash_key, value=hash_data)
    r.expire(name=hash_name, time=ttl)


def get_forecasting_data(data, target, meta):#,context= LambdaContext()):
    try:
        '''global PROJECT_PATH
        #context.callbackWaitsForEmptyEventLoop = False
        # Read Raw data
        if not isaws:
            # PROJECT_PATH = PROJECT_PATH + "/forecasting"
            content = (open(event, 'r'))
            contents = str(content.read())
            event = {}
            event["body"] = contents
        # create features
        data, target, meta = create_features(event)#["body"])
        del event '''

        # Get mlRec, targetRef, modelType from meta of the data
        probStatement = meta["problemStatement"]
        targetRef = str(meta["targetRef"]).replace("@", "").replace(":", "")
        print("Project",str(meta["targetRef"]))
        print("Project",str(meta["targetRef"]).split(":")[2])
        projectName = str(meta["targetRef"]).split(":")[1]
        modelType = meta["modelType"]
        quantiles = int(meta["predictionInterval"])
        print(str("probStatements."+probStatement.replace(" ", "")))

        # import model for given problem statement
        model = srm.download_file( [probStatement.replace(" ", "_")+"_PI" + ".sav"])
        if not model or data.empty:
            return {
                'statusCode' : 200,
                "body": json.dumps({"status": "Missing either model or data.","result": None})
            }
        filename = meta["problemStatement"].replace(" ", "_")+"_"+targetRef.replace(" ", "_")+"_"+modelType
        filenames = [filename+"_lower_PI.dat", filename+"_upper_PI.dat"]
        print(str(type(model)))

        # train model
        stats, model = train_model(model[0], data, target, filename,quantiles, filenames)
        # upload a train mdoel to S3 bucket for future predictions
        # srm.upload_file(model,filenames)
        stats["model_type"] = modelType
        # for memory optimization del all the object created and perform garbage collection
        del model, data, target
        gc.collect()

        # Add job status to redis cache
        job = get_current_job()
        put_data_redis_cache(projectName, job.id, json.dumps({"result": json.dumps(stats),"status": "ok"}))

        return stats if not isaws else {
                                        'statusCode': 200,
                                        'body': json.dumps({"result": json.dumps(stats),"status": "ok"})
                                        }
    except (TypeError,NameError,ValueError,ImportError,RuntimeError,KeyError) as e:
        job = get_current_job()
        put_data_redis_cache(projectName, job.id, json.dumps({"status": str(e), "result": None}))

        return {
            'statusCode': 200,

            'body': json.dumps({"status": str(e), "result": None})
        }


# Model prediction
def predict_forecast(event):#,context= LambdaContext()):
    try:
        global PROJECT_PATH
        #context.callbackWaitsForEmptyEventLoop = False
        if not isaws:
            # PROJECT_PATH = PROJECT_PATH + "/forecasting"
            content = (open(event, 'r'))
            contents = str(content.read())
            event = {}
            event["body"] = contents
        # create features
        data, target, meta = create_features(event)
        del event

        # Get mlRec, targetRef, modelType from meta of the data
        probStatement = meta["problemStatement"]
        targetRef = str(meta["targetRef"]).replace("@", "").replace(":", "")
        modelType = meta["modelType"]
        quantiles = int(meta["predictionInterval"])
        filename = probStatement.replace(" ","_")+"_"+targetRef.replace(" ","_")+"_"+modelType
        filenames = [filename + "_lower_PI.dat", filename + "_upper_PI.dat"]
        model = srm.download_file(filenames)
        if not model or data.empty:
            return {
                'statusCode': 200,
                "body": json.dumps({"status": "Missing either model or data.","result": None}),

            }
        # predict values
        df = predict_data(data,model,quantiles,filenames)
        # for memory optimization del all the object created and perform garbage collection
        del model, data, target
        gc.collect()
        return {
            'statusCode': 200,
            'body': json.dumps({"result": df.to_json(orient='records'),"status":"ok"})
        }
    except (TypeError,NameError,ValueError,ImportError,RuntimeError,KeyError) as e:
        print(e)
        return {
            'statusCode': 200, # all exception are send with status 200 so
            # to write exception error to output point. Sending actual exception code breaks the job flow on SS.
            'body': json.dumps({"status": str(e),"result": None})
        }


def train_model(model,data,target,filepath,quantile,filenames):

    # split data train and test to model score
    quantile_loss = []
    models = []
    train_pct_index = int(0.85 * len(data))
    X_train, X_test = data[:train_pct_index].copy(), data[train_pct_index:].copy()
    y_train, y_test = target[:train_pct_index], target[train_pct_index:]
    quantiles = [(1-quantile/100)/2, 1-(1-quantile/100)/2]

    # Train model using train data
    #X_train["const"] = 1 #sm.add_constant(X_train)
    #X_test["const"] = 1 #sm.add_constant(X_test)
    #data = sm.add_constant(data)
    temp = copy.deepcopy(model)
    print(quantiles)
    i = 0
    for q in quantiles:

        model_train = pi.train_quantile(model, data, target,q)  # Train model using entire data
        # print("trained model",type(model_train))
        temp = pi.train_quantile(temp, X_train, y_train,q)  # Train model using training set
        srm.upload_file([model_train],[filenames[i]])
        # models.append(model_train)
        i += 1
        y_predict = pi.predict_quantile(temp,X_test,q)
        quantile_loss.extend(pi.quantile_loss(q,y_test,y_predict))

    rms = sum(quantile_loss)/ len(quantile_loss)

    d = {"total_training_data_points": str(len(data)), "algorithm": str(type(model)),
         "lower_bound": quantile_loss[0], "upper_bound" : quantile_loss[-1]
        , "rmse": str(rms), "normalised_rmse": str(rms / (y_test.mean()) * 100)}

    del temp, X_train, X_test, y_train, y_test
    stats = d #pd.DataFrame([d])
    # model = (model,rmse_per_hour)
    print(stats,models)
    return stats, models


def predict_data(data,models,quantile,filenames):
    # with open(filepath, "rb") as f:
    #     model = pickle.load(f)
    #     rmse_per_hour = pickle.load(f)
    quantiles = [(1 - quantile / 100) / 2, 1 - (1 - quantile / 100) / 2]
    #data["const"] = 1  # add constant column
    model_lower_pi = srm.download_file([filenames[0]])[0]  # lower bound model
    model_upper_pi = srm.download_file([filenames[1]])[0]  # upper bound model
    logging.info(model_lower_pi)
    logging.info(model_upper_pi)
    y_predict_lower_pi = pi.predict_quantile(model_lower_pi,data,quantiles[0])
    y_predict_upper_pi = pi.predict_quantile(model_upper_pi, data, quantiles[1])
    # df = pd.DataFrame({"hour":X_test["hour"],"day_week":X_test["day_week"],"predict":y_predict,"actual":y_test})
    data = data.reset_index()
    data["predicted_value_lower"] = y_predict_lower_pi
    data["predicted_value_upper"] = y_predict_upper_pi
    # data = data.merge(rmse_per_hour, on=["day_week", "hour"], )
    data = data.drop(data.columns[~data.columns.isin(["predicted_value_lower","predicted_value_upper","date"])], axis=1)
    data["date"] = data["date"].astype("str")
    # for memory optimization del all the object created and perform garbage collection
    del y_predict_lower_pi, y_predict_upper_pi, model_lower_pi, model_upper_pi
    gc.collect()
    return data


if __name__ == '__main__':
    print(get_forecasting_data("C:/Users/Prajakta Gujarathi/Desktop/test_max_save.txt"))

