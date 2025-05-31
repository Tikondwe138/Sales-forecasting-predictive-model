import pandas as pd

def load_and_prepare_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    df.index.freq = 'MS'  # Set frequency to Monthly Start
    df.columns = df.columns.str.strip()
    df = df.dropna()
    return df
