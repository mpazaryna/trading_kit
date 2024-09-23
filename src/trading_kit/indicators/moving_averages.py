from typing import Union

import pandas as pd


def calculate_sma(data: pd.Series, window: int) -> pd.Series:
    """Calculate Simple Moving Average."""
    return data.rolling(window=window).mean()


def calculate_wma(data: pd.Series, window: int) -> pd.Series:
    """Calculate Weighted Moving Average."""
    weights = pd.Series(range(1, window + 1))  # Create weights [1, 2, ..., window]
    return data.rolling(window).apply(
        lambda prices: (prices * weights).sum() / weights.sum(), raw=True
    )


def calculate_wma_precision(
    data: pd.Series, window: int, precision: int = 2
) -> pd.Series:
    """
    Calculate Weighted Moving Average (WMA) with variable precision.

    This function computes the Weighted Moving Average of a given pandas Series,
    allowing for a specified level of precision in the results. The WMA gives
    higher weights to more recent data points within the specified window.

    Parameters:
    -----------
    data : pd.Series
        A pandas Series containing the financial data (typically price data).
        The index of this Series is expected to be in chronological order.

    window : int
        The size of the moving window. This determines how many previous data
        points are considered in each WMA calculation. Must be a positive integer.

    precision : int, optional (default=2)
        The number of decimal places to round the results to. This allows for
        adjustable precision based on the specific requirements of the trading
        strategy or the asset being analyzed.

    Returns:
    --------
    pd.Series
        A pandas Series containing the calculated Weighted Moving Average values.
        The resulting Series will have the same index as the input data.

    Notes:
    ------
    - The function uses a linear weighting scheme where the most recent data point
      in each window has the highest weight (equal to the window size), and the
      oldest data point has a weight of 1.
    - The first (window - 1) elements of the returned Series will be NaN, as there
      are not enough previous data points to calculate the WMA.
    - This function is particularly useful in financial applications where the
      required precision may vary based on the asset type, trading frequency,
      or regulatory requirements.

    Examples:
    ---------
    >>> data = pd.Series([100, 102, 104, 106, 108])
    >>> calculate_wma_precision(data, window=3, precision=2)
    0      NaN
    1      NaN
    2    102.67
    3    104.67
    4    106.67
    dtype: float64

    >>> calculate_wma_precision(data, window=3, precision=4)
    0         NaN
    1         NaN
    2    102.6667
    3    104.6667
    4    106.6667
    dtype: float64
    """
    weights = pd.Series(range(1, window + 1))
    wma = data.rolling(window).apply(
        lambda prices: (prices * weights).sum() / weights.sum(), raw=True
    )
    return wma.round(precision)
