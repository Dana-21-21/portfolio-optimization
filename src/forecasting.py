from statsmodels.tsa.arima.model import ARIMA
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
)

import numpy as np


def train_arima(train, order=(0,1,0)):
    """
    Train ARIMA model.
    """

    model = ARIMA(train, order=order)

    return model.fit()


def forecast(model, steps):
    """
    Generate forecasts from a fitted ARIMA model.
    """
    return model.get_forecast(steps=steps)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
)

import numpy as np


def evaluate(actual, predicted):
    """
    Evaluate forecasting performance.

    Parameters
    ----------
    actual : pandas.Series
        Actual observed values.

    predicted :
        Either a pandas Series or a PredictionResultsWrapper.

    Returns
    -------
    dict
    """

    # If ARIMA get_forecast() object is supplied
    if hasattr(predicted, "predicted_mean"):
        predicted = predicted.predicted_mean

    mae = mean_absolute_error(actual, predicted)

    rmse = np.sqrt(
        mean_squared_error(actual, predicted)
    )

    mape = mean_absolute_percentage_error(
        actual,
        predicted
    ) * 100

    return {
        "MAE": mae,
        "RMSE": rmse,
        "MAPE": mape
    }
