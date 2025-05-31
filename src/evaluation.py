from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_forecast(true_values, predicted_values):
    """
    Calculate evaluation metrics: MAE and RMSE.
    """
    mae = mean_absolute_error(true_values, predicted_values)
    mse = mean_squared_error(true_values, predicted_values)
    rmse = np.sqrt(mse)  # ✅ this line replaces `squared=False`
    return {'MAE': mae, 'RMSE': rmse}

def print_evaluation_metrics(metrics, model_name="Model"):
    """
    Print evaluation metrics in a readable format.
    """
    print(f"{model_name} Evaluation:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.2f}")
