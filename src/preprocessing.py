# src/preprocessing.py
import pandas as pd

def load_and_prepare_data(filepath):
    """
    Load sales data CSV, parse dates, set index, and do basic cleaning.

    Args:
        filepath (str): Path to CSV file.

    Returns:
        pd.DataFrame: Cleaned sales data with Date as index.
    """
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df.set_index('Date', inplace=True)

    # Check and handle missing values if any (for demo, just drop)
    df = df.dropna()

    return df
