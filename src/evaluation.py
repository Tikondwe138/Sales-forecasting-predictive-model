# src/evaluation.py
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_forecast(true_values, predicted_values):
    """
    Calculate evaluation metrics: MAE and RMSE.

    Args:
        true_values (pd.Series or np.array): Actual values.
        predicted_values (pd.Series or np.array): Forecasted values.

    Returns:
        dict: Dictionary with MAE and RMSE scores.
    """
    mae = mean_absolute_error(true_values, predicted_values)
    rmse = mean_squared_error(true_values, predicted_values, squared=False)
    return {'MAE': mae, 'RMSE': rmse}

def print_evaluation_metrics(metrics, model_name="Model"):
    """
    Print evaluation metrics in a readable format.

    Args:
        metrics (dict): Dictionary with metric names and values.
        model_name (str): Name of the model for labeling output.
    """
    print(f"{model_name} Evaluation:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.2f}")
