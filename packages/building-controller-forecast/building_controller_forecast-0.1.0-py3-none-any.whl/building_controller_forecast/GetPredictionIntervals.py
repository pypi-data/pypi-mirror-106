
import numpy as np
import statsmodels.api as sm

from scipy.stats import norm
import pandas as pd


def ols_quantile_prediction(m, X, q):
    # m: OLS model.
    # X: X matrix.
    # q: Quantile.
    #
    # Set alpha based on q. Vectorized for different values of q.
    mean_pred = m.predict(X.reindex(columns= m.model.data.param_names))
    se = np.sqrt(m.scale)
    result = mean_pred + norm.ppf(q) * se
    return result.values


def rf_quantile_prediction(m, X, q):
        rf_preds = []
        for estimator in m.estimators_:
            rf_preds.append(estimator.predict(X))
        rf_preds = np.array(rf_preds).transpose()  # One row per record.
        return np.percentile(rf_preds, q * 100, axis=1)


def gb_quantile_prediction(m, X, q):
    return m.predict(X)


def reg_quntile_prediction(m,X,q):
    m = m.fit(q=q)
    print(m.summary(),m.model.data.param_names)
    result = m.predict(X.reindex(columns= m.model.data.param_names))

    return result.values


def ols_quantile_training(m, X, y, q):
    m = sm.OLS(y, X).fit()
    return m


def rf_quantile_training(m, X, y, q):
    m.fit(X, y)
    return m


def gb_quantile_training(m, X, y, q):
    m.alpha = q
    return m.fit(X, y)
    return m


def reg_quntile_training(m, X, y, q):
    quantreg =sm.QuantReg(y, X) # sm.QuantReg(y.as_matrix(), X.as_matrix())
    return quantreg


# pandas version rather than Keras.
def quantile_loss(q, y, f):
    # q: Quantile to be evaluated, e.g., 0.5 for median.
    # y: True value.
    # f: Fitted or predicted value.
    e = y - f
    return np.maximum(q * e, (q - 1) * e)


def predict_quantile(model, X, q):
    method = str(type(model)).split(".")[-1]
    print("getPrediction prediction", method)
    if "RandomForestRegressor" in method:
        return rf_quantile_prediction(model, X, q)
    if "QuantReg" in method:
        return reg_quntile_prediction(model,X, q)
    if "GradientBoostingRegressor" in method:
        return gb_quantile_prediction(model, X, q)
    else:
        X["const"] = 1
        return ols_quantile_prediction(model, X, q)


def train_quantile(model, X, y, q):
    method = str(type(model)).split(".")[-1]
    print("getPrediction training",method)
    if "RandomForestRegressor" in method:
        return rf_quantile_training(model, X, y, q)
    if "QuantReg" in method:
        return reg_quntile_training(model,X, y, q)
    if "GradientBoostingRegressor" in method:
        return gb_quantile_training(model, X, y, q)
    else:
        X["const"] = 1
        return ols_quantile_training(model, X, y, q)




