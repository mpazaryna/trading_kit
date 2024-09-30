from datetime import datetime
from typing import Dict, List, Tuple


def api_friendly_analyze_stock_trends(
    dates: List[str],
    prices: List[float],
    short_window: int = 10,
    long_window: int = 30,
    precision: int = 2,
) -> Dict[str, List[float]]:
    """
    Analyze stock price trends using Weighted Moving Averages (WMA) with API-friendly input and output.

    This function calculates short-term and long-term Weighted Moving Averages
    for a given series of stock prices. It then generates buy/sell signals
    based on the crossover of these moving averages.

    Parameters:
    -----------
    dates : List[str]
        A list of date strings in 'YYYY-MM-DD' format.
    prices : List[float]
        A list of daily closing prices of a stock.
    short_window : int, optional (default=10)
        The window size for the short-term WMA, typically 10-20 days.
    long_window : int, optional (default=30)
        The window size for the long-term WMA, typically 20-50 days.
    precision : int, optional (default=2)
        The number of decimal places to round the WMA results.

    Returns:
    --------
    Dict[str, List[float]]
        A dictionary containing:
        - 'short_wma': List of short-term WMA values
        - 'long_wma': List of long-term WMA values
        - 'signals': List of buy/sell signals (1 for buy, -1 for sell, 0 for hold)

    Notes:
    ------
    - Buy signals are generated when the short-term WMA crosses above the long-term WMA.
    - Sell signals are generated when the short-term WMA crosses below the long-term WMA.
    - The first `long_window - 1` elements will have None values for signals.
    """

    def calculate_wma(data: List[float], window: int) -> List[float]:
        result = []
        for i in range(len(data)):
            if i < window - 1:
                result.append(None)
            else:
                weights = list(range(1, window + 1))
                wma = sum(
                    data[i - window + 1 : i + 1][j] * weights[j] for j in range(window)
                ) / sum(weights)
                result.append(round(wma, precision))
        return result

    short_wma = calculate_wma(prices, short_window)
    long_wma = calculate_wma(prices, long_window)

    signals = [None] * (long_window - 1)
    for i in range(long_window - 1, len(prices)):
        if short_wma[i] > long_wma[i]:
            signals.append(1)  # Buy signal
        elif short_wma[i] < long_wma[i]:
            signals.append(-1)  # Sell signal
        else:
            signals.append(0)  # Hold

    return {"short_wma": short_wma, "long_wma": long_wma, "signals": signals}
