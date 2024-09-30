from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd

from trading_kit.indicators.moving_averages import calculate_wma_precision


def analyze_stock_trends(
    prices: pd.Series, short_window: int = 10, long_window: int = 30, precision: int = 2
) -> Tuple[pd.Series, pd.Series, pd.Series]:
    """
    Analyze stock price trends using Weighted Moving Averages (WMA).

    This function calculates short-term and long-term Weighted Moving Averages
    for a given series of stock prices. It then generates buy/sell signals
    based on the crossover of these moving averages.

    Parameters:
    -----------
    prices : pd.Series
        A pandas Series containing daily closing prices of a stock.
        The index should be a DatetimeIndex in chronological order.

    short_window : int, optional (default=10)
        The window size for the short-term WMA, typically 10-20 days.

    long_window : int, optional (default=30)
        The window size for the long-term WMA, typically 20-50 days.

    precision : int, optional (default=2)
        The number of decimal places to round the WMA results.

    Returns:
    --------
    Tuple[pd.Series, pd.Series, pd.Series]
        A tuple containing three pandas Series:
        1. Short-term WMA
        2. Long-term WMA
        3. Buy/Sell signals (1 for buy, -1 for sell, 0 for hold)

    Notes:
    ------
    - The function uses the calculate_wma_precision function to compute WMAs.
    - Buy signals are generated when the short-term WMA crosses above the long-term WMA.
    - Sell signals are generated when the short-term WMA crosses below the long-term WMA.
    - The first `long_window - 1` elements will have NaN values for signals.

    Example:
    --------
    >>> import pandas as pd
    >>> import numpy as np
    >>>
    >>> # Generate sample price data
    >>> dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
    >>> prices = pd.Series(np.random.randn(100).cumsum() + 100, index=dates)
    >>>
    >>> # Analyze trends
    >>> short_wma, long_wma, signals = analyze_stock_trends(prices)
    >>>
    >>> # Print results
    >>> print(short_wma.head())
    >>> print(long_wma.head())
    >>> print(signals.value_counts())
    """
    # Calculate short-term and long-term WMAs
    short_wma = calculate_wma_precision(
        prices, window=short_window, precision=precision
    )
    long_wma = calculate_wma_precision(prices, window=long_window, precision=precision)

    # Generate buy/sell signals
    signals = pd.Series(0, index=prices.index)
    signals[short_wma > long_wma] = 1  # Buy signal
    signals[short_wma < long_wma] = -1  # Sell signal

    # Set signals to NaN for the initial period where we don't have both WMAs
    signals[: long_window - 1] = np.nan

    return short_wma, long_wma, signals


def analyze_stock_trends_from_json(
    data: Dict[str, Any],
    short_window: int = 10,
    long_window: int = 30,
    precision: int = 2,
) -> Tuple[pd.Series, pd.Series, pd.Series]:
    """
    Analyze stock price trends using Weighted Moving Averages (WMA) from JSON data.

    This function calculates short-term and long-term Weighted Moving Averages
    for a given series of stock prices provided in JSON format. It then generates
    buy/sell signals based on the crossover of these moving averages.

    Parameters:
    -----------
    data : dict
        A dictionary containing stock price data in JSON format. The dictionary
        should have a key 'prices' with a list of price values and a key 'dates'
        with a list of corresponding date strings.

    short_window : int, optional (default=10)
        The window size for the short-term WMA, typically 10-20 days.

    long_window : int, optional (default=30)
        The window size for the long-term WMA, typically 20-50 days.

    precision : int, optional (default=2)
        The number of decimal places to round the WMA results.

    Returns:
    --------
    Tuple[pd.Series, pd.Series, pd.Series]
        A tuple containing three pandas Series:
        1. Short-term WMA
        2. Long-term WMA
        3. Buy/Sell signals (1 for buy, -1 for sell, 0 for hold)

    Notes:
    ------
    - The function uses the calculate_wma_precision function to compute WMAs.
    - Buy signals are generated when the short-term WMA crosses above the long-term WMA.
    - Sell signals are generated when the short-term WMA crosses below the long-term WMA.
    - The first `long_window - 1` elements will have NaN values for signals.

    Example:
    --------
    >>> data = {
    >>>     "dates": ["2023-01-01", "2023-01-02", "2023-01-03", ...],
    >>>     "prices": [100.0, 101.5, 102.3, ...]
    >>> }
    >>> short_wma, long_wma, signals = analyze_stock_trends_from_json(data)
    >>> print(short_wma.head())
    >>> print(long_wma.head())
    >>> print(signals.value_counts())
    """
    # Convert JSON data to pandas Series
    dates = pd.to_datetime(data["dates"])
    prices = pd.Series(data["prices"], index=dates)

    # Calculate short-term and long-term WMAs
    short_wma = calculate_wma_precision(
        prices, window=short_window, precision=precision
    )
    long_wma = calculate_wma_precision(prices, window=long_window, precision=precision)

    # Generate buy/sell signals
    signals = pd.Series(0, index=prices.index)
    signals[short_wma > long_wma] = 1  # Buy signal
    signals[short_wma < long_wma] = -1  # Sell signal

    # Set signals to NaN for the initial period where we don't have both WMAs
    signals[: long_window - 1] = np.nan

    return short_wma, long_wma, signals
