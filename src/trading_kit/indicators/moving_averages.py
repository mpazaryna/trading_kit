import pandas as pd  # Add this import


def calculate_sma(data: pd.Series, window: int) -> pd.Series:
    """Calculate Simple Moving Average."""
    return data.rolling(window=window).mean()
