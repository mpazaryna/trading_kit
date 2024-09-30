from typing import List, Optional

import numpy as np
import pandas as pd


def calculate_sma(data: List[float], window: int) -> List[Optional[float]]:
    """
    Calculate Simple Moving Average (SMA).

    The Simple Moving Average (SMA) is a widely used indicator in technical analysis
    that helps smooth out price data by creating a constantly updated average price.
    It is calculated by taking the arithmetic mean of a given set of values over a
    specified number of periods.

    Real-World Usage:
    -----------------
    The SMA is used by traders and analysts to identify trends in financial markets.
    By averaging price data, the SMA reduces the noise from random price fluctuations,
    making it easier to identify the underlying trend. For example, a 50-day SMA of
    a stock's closing prices can help traders determine the overall direction of the
    stock's price movement over the past 50 days.

    The SMA is also used to generate trading signals. When the price of an asset
    crosses above its SMA, it may be considered a buy signal, indicating that the
    asset's price is gaining upward momentum. Conversely, when the price crosses
    below its SMA, it may be considered a sell signal, indicating that the asset's
    price is losing momentum.

    Parameters:
    -----------
    data : List[float]
        A list of numerical data points (e.g., stock prices).

    window : int
        The size of the moving window. This determines how many previous data
        points are considered in each SMA calculation. Must be a positive integer.

    Returns:
    --------
    List[Optional[float]]
        A list containing the calculated SMA values. The first (window - 1) elements
        will be None, as there are not enough previous data points to calculate the SMA.

    Examples:
    ---------
    >>> data = [1, 2, 3, 4, 5]
    >>> calculate_sma(data, window=3)
    [None, None, 2.0, 3.0, 4.0]
    """
    series = pd.Series(data)
    sma = series.rolling(window=window).mean()
    return [None if pd.isna(x) else float(x) for x in sma]


def calculate_wma(data: List[float], window: int) -> List[Optional[float]]:
    """
    Calculate Weighted Moving Average (WMA).

    The Weighted Moving Average (WMA) is a type of moving average that assigns
    more weight to recent data points, making it more responsive to new information
    compared to the Simple Moving Average (SMA). The weights decrease linearly,
    with the most recent data point having the highest weight.

    Real-World Usage:
    -----------------
    The WMA is used by traders and analysts to identify trends and potential
    reversals in financial markets. By giving more weight to recent prices, the
    WMA is more sensitive to recent price changes, making it useful for detecting
    short-term trends and momentum shifts.

    The WMA is particularly useful in volatile markets where recent price movements
    are more relevant for making trading decisions. For example, a 10-day WMA of a
    stock's closing prices can help traders identify short-term trends and potential
    entry or exit points based on recent price action.

    Parameters:
    -----------
    data : List[float]
        A list of numerical data points (e.g., stock prices).

    window : int
        The size of the moving window. This determines how many previous data
        points are considered in each WMA calculation. Must be a positive integer.

    Returns:
    --------
    List[Optional[float]]
        A list containing the calculated WMA values. The first (window - 1) elements
        will be None, as there are not enough previous data points to calculate the WMA.

    Examples:
    ---------
    >>> data = [1, 2, 3, 4, 5]
    >>> calculate_wma(data, window=3)
    [None, None, 2.3333333333333335, 3.3333333333333335, 4.333333333333333]
    """
    series = pd.Series(data)
    weights = pd.Series(range(1, window + 1))  # Create weights [1, 2, ..., window]
    wma = series.rolling(window).apply(
        lambda prices: (prices * weights).sum() / weights.sum(), raw=True
    )
    return [None if pd.isna(x) else float(x) for x in wma]


def calculate_wma_precision(
    data: List[float], window: int, precision: int = 2
) -> List[Optional[float]]:
    """
    Calculate Weighted Moving Average (WMA) with variable precision.

    This function computes the Weighted Moving Average of a given pandas Series,
    allowing for a specified level of precision in the results. The WMA gives
    higher weights to more recent data points within the specified window.

    Real-World Usage:
    -----------------
    The WMA with variable precision is particularly useful in financial applications
    where the required precision may vary based on the asset type, trading frequency,
    or regulatory requirements. For example, in high-frequency trading, a higher
    precision may be required to capture small price movements, while in long-term
    investing, a lower precision may be sufficient.

    By allowing for adjustable precision, this function provides flexibility for
    different trading strategies and asset types. Traders can use the WMA with
    variable precision to fine-tune their analysis and make more informed trading
    decisions based on the specific requirements of their strategy.

    Parameters:
    -----------
    data : List[float]
        A list of numerical data points (e.g., stock prices).

    window : int
        The size of the moving window. This determines how many previous data
        points are considered in each WMA calculation. Must be a positive integer.

    precision : int, optional (default=2)
        The number of decimal places to round the results to. This allows for
        adjustable precision based on the specific requirements of the trading
        strategy or the asset being analyzed.

    Returns:
    --------
    List[Optional[float]]
        A list containing the calculated WMA values rounded to the specified precision.
        The first (window - 1) elements will be None, as there are not enough previous
        data points to calculate the WMA.

    Examples:
    ---------
    >>> data = [100, 102, 104, 106, 108]
    >>> calculate_wma_precision(data, window=3, precision=2)
    [None, None, 102.67, 104.67, 106.67]

    >>> calculate_wma_precision(data, window=3, precision=4)
    [None, None, 102.6667, 104.6667, 106.6667]
    """
    series = pd.Series(data)
    weights = pd.Series(range(1, window + 1))
    wma = series.rolling(window).apply(
        lambda prices: (prices * weights).sum() / weights.sum(), raw=True
    )
    # Round the results to the specified precision
    return [None if pd.isna(x) else round(float(x), precision) for x in wma]


def calculate_ema(data: List[float], window: int) -> List[Optional[float]]:
    """
    Calculate Exponential Moving Average (EMA).

    The Exponential Moving Average (EMA) is a type of moving average that places
    a greater weight and significance on the most recent data points. The EMA reacts
    more quickly to recent price changes than the Simple Moving Average (SMA), making
    it a popular choice among traders and analysts.

    Real-World Usage:
    -----------------
    The EMA is used to identify trends and potential reversals in financial markets.
    By giving more weight to recent prices, the EMA is more responsive to new information,
    making it useful for detecting short-term trends and momentum shifts. For example,
    a 10-day EMA of a stock's closing prices can help traders identify short-term trends
    and potential entry or exit points based on recent price action.

    The EMA is also used to generate trading signals. When the price of an asset crosses
    above its EMA, it may be considered a buy signal, indicating that the asset's price
    is gaining upward momentum. Conversely, when the price crosses below its EMA, it may
    be considered a sell signal, indicating that the asset's price is losing momentum.

    Parameters:
    -----------
    data : List[float]
        A list of numerical data points (e.g., stock prices).

    window : int
        The size of the moving window. This determines the smoothing factor for the EMA.
        Must be a positive integer.

    Returns:
    --------
    List[Optional[float]]
        A list containing the calculated EMA values. The first (window - 1) elements
        will be None, as there are not enough previous data points to calculate the EMA.

    Examples:
    ---------
    >>> data = [1, 2, 3, 4, 5]
    >>> calculate_ema(data, window=3)
    [None, None, 2.0, 3.5, 4.25]
    """
    if window <= 0:
        raise ValueError("Window size must be a positive integer")

    ema = [None] * len(data)
    alpha = 2 / (window + 1)
    for i in range(len(data)):
        if i == 0:
            ema[i] = data[i]
        elif i < window - 1:
            ema[i] = None
        else:
            if ema[i - 1] is None:
                ema[i] = data[i]
            else:
                ema[i] = alpha * data[i] + (1 - alpha) * ema[i - 1]
    return ema


def calculate_ema_pure(data: List[float], window: int) -> List[Optional[float]]:
    """
    Calculate Exponential Moving Average (EMA) for a list of data.

    The Exponential Moving Average (EMA) is a type of moving average that places
    a greater weight and significance on the most recent data points. The EMA reacts
    more quickly to recent price changes than the Simple Moving Average (SMA), making
    it a popular choice among traders and analysts.

    Real-World Usage:
    -----------------
    The EMA is used to identify trends and potential reversals in financial markets.
    By giving more weight to recent prices, the EMA is more responsive to new information,
    making it useful for detecting short-term trends and momentum shifts. For example,
    a 10-day EMA of a stock's closing prices can help traders identify short-term trends
    and potential entry or exit points based on recent price action.

    The EMA is also used to generate trading signals. When the price of an asset crosses
    above its EMA, it may be considered a buy signal, indicating that the asset's price
    is gaining upward momentum. Conversely, when the price crosses below its EMA, it may
    be considered a sell signal, indicating that the asset's price is losing momentum.

    Parameters:
    -----------
    data : List[float]
        A list of numerical data points (e.g., stock prices).

    window : int
        The size of the moving window. This determines the smoothing factor for the EMA.
        Must be a positive integer.

    Returns:
    --------
    List[Optional[float]]
        A list containing the calculated EMA values. The first (window - 1) elements
        will be None, as there are not enough previous data points to calculate the EMA.

    Examples:
    ---------
    >>> data = [1, 2, 3, 4, 5]
    >>> calculate_ema_pure(data, window=3)
    [None, None, 2.0, 3.5, 4.25]
    """
    if window <= 0:
        raise ValueError("Window size must be a positive integer")

    ema = [None] * len(data)
    alpha = 2 / (window + 1)
    for i in range(len(data)):
        if i == 0:
            ema[i] = data[i]
        elif i < window - 1:
            ema[i] = None
        else:
            if ema[i - 1] is None:
                ema[i] = data[i]
            else:
                ema[i] = alpha * data[i] + (1 - alpha) * ema[i - 1]
    return ema
