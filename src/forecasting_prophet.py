# src/forecasting_prophet.py
import pandas as pd
from prophet import Prophet

def prepare_prophet_data(df):
    """
    Prepare DataFrame for Prophet by renaming columns.

    Args:
        df (pd.DataFrame): DataFrame with sales data and Date as index.

    Returns:
        pd.DataFrame: DataFrame with columns ['ds', 'y'] for Prophet.
    """
    prophet_df = df.reset_index().rename(columns={'Date': 'ds', 'Sales': 'y'})
    return prophet_df

def train_prophet_model(prophet_df):
    """
    Train Prophet forecasting model.

    Args:
        prophet_df (pd.DataFrame): Data prepared for Prophet.

    Returns:
        Prophet: Trained Prophet model.
    """
    model = Prophet(yearly_seasonality=True, daily_seasonality=False, weekly_seasonality=False)
    model.fit(prophet_df)
    return model

def make_forecast(model, periods, freq='MS'):
    """
    Create future dataframe and forecast using Prophet.

    Args:
        model (Prophet): Trained Prophet model.
        periods (int): Number of future periods to forecast.
        freq (str): Frequency string, default monthly start 'MS'.

    Returns:
        pd.DataFrame: Forecast DataFrame with predictions.
    """
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    return forecast
