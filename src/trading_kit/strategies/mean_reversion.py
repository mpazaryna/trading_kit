# trading_kit/strategies/mean_reversion.py

from typing import List

import pandas as pd


def calculate_z_score(data: List[float]) -> List[float]:
    """
    Calculate the Z-score of a given data series.

    The Z-score indicates how many standard deviations an element is from the mean.
    In stock trading, it helps identify overbought or oversold conditions.

    Args:
        data (List[float]): The input price data series (e.g., closing prices of a stock).

    Returns:
        List[float]: The Z-score of the input data, which can be used to assess price deviations.
    """
    data_series = pd.Series(data)
    z_scores = (data_series - data_series.mean()) / data_series.std()
    return z_scores.tolist()


def generate_mean_reversion_signals(
    data: List[float], entry_threshold: float = 1.0, exit_threshold: float = 0.0
) -> List[int]:
    """
    Generate trading signals based on a mean reversion strategy.

    This strategy assumes that prices will revert to their mean over time.
    A buy signal is generated when the price is significantly below the mean (indicating it may be undervalued),
    and a sell signal is generated when the price is significantly above the mean (indicating it may be overvalued).

    Args:
        data (List[float]): The input price data series (e.g., closing prices of a stock).
        entry_threshold (float): The Z-score threshold for entering a position (default is 1.0).
        exit_threshold (float): The Z-score threshold for exiting a position (default is 0.0).

    Returns:
        List[int]: A list of trading signals (-1 for sell, 1 for buy, 0 for hold).
        A buy signal (1) indicates a potential long position,
        a sell signal (-1) indicates a potential short position,
        and a hold signal (0) indicates no action.
    """
    z_scores = calculate_z_score(data)
    signals = [0] * len(data)

    for i, z in enumerate(z_scores):
        if z < -entry_threshold:
            signals[i] = 1  # Buy signal
        elif z > entry_threshold:
            signals[i] = -1  # Sell signal
        elif -exit_threshold <= z <= exit_threshold:
            signals[i] = 0  # Hold signal

    return signals


# Additional functions for the strategy can be added here...
