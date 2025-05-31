from src.preprocessing import load_and_prepare_data
from src.forecasting_arima import run_arima
from src.forecasting_prophet import run_prophet
from src.evaluation import evaluate_forecast, print_evaluation_metrics

def main():
    print("[INFO] Loading and cleaning data...")
    df = load_and_prepare_data("data/sales_data.csv")

    forecast_steps = 12

    # ARIMA Forecast
    print("\n[INFO] Running ARIMA forecast...")
    arima_forecast = run_arima(df, forecast_steps=forecast_steps)
    arima_true = df['Sales'].tail(forecast_steps)
    arima_metrics = evaluate_forecast(arima_true, arima_forecast)
    print_evaluation_metrics(arima_metrics, model_name="ARIMA")

    # Prophet Forecast
    print("\n[INFO] Running Prophet forecast...")
    prophet_forecast_df = run_prophet(df, forecast_steps=forecast_steps)
    prophet_true = df['Sales'].tail(forecast_steps)
    prophet_predicted = prophet_forecast_df['yhat'].values  # convert to array

    prophet_metrics = evaluate_forecast(prophet_true, prophet_predicted)
    print_evaluation_metrics(prophet_metrics, model_name="Prophet")

    print("\n[INFO] Forecasting complete.")

if __name__ == "__main__":
    main()
