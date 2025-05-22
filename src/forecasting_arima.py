# src/forecasting_arima.py
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(train_series, order=(2,1,2)):
    """
    Train an ARIMA model on the training data.

    Args:
        train_series (pd.Series): Time series training data.
        order (tuple): ARIMA order (p,d,q).

    Returns:
        ARIMAResultsWrapper: Fitted ARIMA model.
    """
    model = ARIMA(train_series, order=order)
    result = model.fit()
    return result

def forecast_arima(model_fit, steps):
    """
    Forecast future values using the trained ARIMA model.

    Args:
        model_fit: Trained ARIMA model object.
        steps (int): Number of periods to forecast.

    Returns:
        pd.Series: Forecasted values.
    """
    forecast = model_fit.forecast(steps=steps)
    return forecast
