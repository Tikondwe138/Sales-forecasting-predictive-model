from src.preprocessing import load_and_prepare_data
from src.forecasting_arima import run_arima
from src.forecasting_prophet import run_prophet
from src.evaluation import evaluate_model

# Load + clean
df = load_and_prepare_data("data/sales_data.csv")

# Run ARIMA
arima_forecast = run_arima(df)
evaluate_model(df, arima_forecast, model_name="ARIMA")

# Run Prophet
prophet_forecast = run_prophet(df)
evaluate_model(df, prophet_forecast, model_name="Prophet")
