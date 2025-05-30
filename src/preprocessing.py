# src/preprocessing.py

import pandas as pd

def load_and_prepare_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    df.columns = df.columns.str.strip()  # Clean weird spaces
    # df.columns = df.columns.str.lower()  # Optional: force lowercase
    df = df.dropna()
    return df
