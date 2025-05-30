# src/forecasting_prophet.py

import pandas as pd
from prophet import Prophet

def prepare_prophet_data(df):
    prophet_df = df.reset_index().rename(columns={'Date': 'ds', 'Sales': 'y'})  # ✅ Match column name
    return prophet_df

def train_prophet_model(prophet_df):
    model = Prophet(yearly_seasonality=True, daily_seasonality=False, weekly_seasonality=False)
    model.fit(prophet_df)
    return model

def make_forecast(model, periods, freq='MS'):
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    return forecast

def run_prophet(df, forecast_steps=12):
    prophet_df = prepare_prophet_data(df)
    model = train_prophet_model(prophet_df)
    forecast = make_forecast(model, forecast_steps)
    return forecast[['ds', 'yhat']]  # Optional: limit to just useful output
