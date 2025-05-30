# src/forecasting_arima.py

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(train_series, order=(2, 1, 2)):
    model = ARIMA(train_series, order=order)
    result = model.fit()
    return result

def forecast_arima(model_fit, steps):
    forecast = model_fit.forecast(steps=steps)
    return forecast

def run_arima(df, target_column="Sales", forecast_steps=12):  # 🧠 capital "S"
    df.index = pd.to_datetime(df.index)
    series = df[target_column]
    model_fit = train_arima_model(series)
    forecast = forecast_arima(model_fit, forecast_steps)
    return forecast
