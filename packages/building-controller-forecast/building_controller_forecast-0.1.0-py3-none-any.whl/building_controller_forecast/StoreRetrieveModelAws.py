try:
    import unzip_requirements
except ImportError:
    pass

import boto3
from io import BytesIO
import pickle
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
import config as cfg
import gc


bucketname = cfg.environment["bucketname"]
s3 = boto3.resource('s3')
my_bucket = s3.Bucket(bucketname)
PROJECT_PATH = ""
FLASK_ENV = os.environ['FLASK_ENV']


# download file from S3 bucket given path and filename
def download_file(model_path):
    try:
        print(model_path)
        models = []
        for i in range(len(model_path)):
            with BytesIO() as d:
                for s3_object in my_bucket.objects.all():
                    path, filename = os.path.split(s3_object.key)
                    if path == FLASK_ENV and filename == model_path[i]:
                        s3.Bucket(bucketname).download_fileobj(s3_object.key, d)
                        d.seek(0)  # move back to the beginning after writing
                        model = pickle.load(d)
                        print(str(type(model)))
                        models.append(model)
        return models if models else False
    except (TypeError,NameError,ValueError,ImportError,RuntimeError) as  e:
        print(e)
        return False


# upload file to s3 bucket
def upload_file(models,filepath):
    for i in range(len(models)):
        with BytesIO() as d:
            method = str(type(models[i])).split(".")[-1]
            d = pickle.dumps(models[i])
            full_path = os.path.join(FLASK_ENV, filepath[i])
            response = s3.Object(bucketname, full_path).put(Body=d)["ResponseMetadata"]
    del models
    gc.collect()
    return response["HTTPStatusCode"]
