import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

from src.preprocessing import load_and_prepare_data
from src.forecasting_arima import run_arima
from src.forecasting_prophet import run_prophet
from src.evaluation import evaluate_forecast

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(page_title="Sales Forecast Dashboard", layout="wide")

# Use Seaborn darkgrid style, invert colors by switching to 'dark_background'
style.use('dark_background')
sns.set_style("darkgrid")

# ---------------------------
# Title & Intro
# ---------------------------
st.title("Sales Forecasting Dashboard")
st.markdown("""
This dashboard presents **sales forecasts** using two popular models:
- **ARIMA:** Traditional statistical time series model.
- **Prophet:** Facebook’s powerful forecasting tool with automatic seasonality detection.

Performance is measured using:
- **MAE:** Mean Absolute Error — average error magnitude.
- **RMSE:** Root Mean Squared Error — penalizes large errors.

Use the sidebar to adjust forecast horizon or data.
""")

# ---------------------------
# Sidebar: User Controls
# ---------------------------
st.sidebar.header("Settings")

data_path = st.sidebar.text_input("CSV Data File Path", value="data/sales_data.csv")
forecast_steps = st.sidebar.slider("Months to Forecast", min_value=1, max_value=24, value=12)

# ---------------------------
# Load & Prepare Data
# ---------------------------
try:
    df = load_and_prepare_data(data_path)
    actual_values = df['Sales'].tail(forecast_steps)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# ---------------------------
# Function: Plot Forecast vs Actual
# ---------------------------
def plot_forecast_vs_actual(dates, actual, predicted, title):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dates, actual, label="Actual", marker='o', color='#00FF00', alpha=0.8)  # bright green
    ax.plot(dates, predicted, label="Forecast", linestyle='--', marker='x', color='#FF6347', alpha=0.9)  # tomato red

    ax.set_title(title, fontsize=14, weight='bold')
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Transparent background
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    return fig

# ---------------------------
# ARIMA Forecast Section
# ---------------------------
st.subheader("ARIMA Forecast")
with st.spinner("Running ARIMA model..."):
    arima_forecast = run_arima(df, forecast_steps=forecast_steps)
    arima_metrics = evaluate_forecast(actual_values, arima_forecast)

st.pyplot(plot_forecast_vs_actual(actual_values.index, actual_values.values, arima_forecast.values, "ARIMA: Actual vs Forecast"))
st.markdown("**ARIMA Forecast Metrics:**")
st.json(arima_metrics)

st.markdown("""
ARIMA is a classical statistical model that tries to capture the dependencies between past sales and predict future sales.
""")

# ---------------------------
# Prophet Forecast Section
# ---------------------------
st.subheader("Prophet Forecast")
with st.spinner("Running Prophet model..."):
    prophet_forecast = run_prophet(df, forecast_steps=forecast_steps)
    prophet_predicted = prophet_forecast['yhat'].tail(forecast_steps).values
    prophet_metrics = evaluate_forecast(actual_values, prophet_predicted)

st.pyplot(plot_forecast_vs_actual(actual_values.index, actual_values.values, prophet_predicted, "Prophet: Actual vs Forecast"))
st.markdown("**Prophet Forecast Metrics:**")
st.json(prophet_metrics)

st.markdown("""
Prophet automatically models trends and seasonality in your sales data, making it powerful for complex time series.
""")

# ---------------------------
# Footer & Final Notes
# ---------------------------
st.info("""
### How to Interpret:
- The graphs show how close each model's forecast is to the actual sales.
- Lower MAE and RMSE mean better forecast accuracy.
- Use the sidebar to experiment with different forecast horizons.
""")

st.success("Forecasting complete. Adjust settings in the sidebar and explore the results!")
