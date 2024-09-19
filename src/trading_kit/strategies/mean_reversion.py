# trading_kit/strategies/mean_reversion.py

from typing import Tuple

import pandas as pd


def calculate_z_score(data: pd.Series) -> pd.Series:
    """
    Calculate the Z-score of a given data series.

    The Z-score indicates how many standard deviations an element is from the mean.
    In stock trading, it helps identify overbought or oversold conditions.

    Args:
        data (pd.Series): The input price data series (e.g., closing prices of a stock).

    Returns:
        pd.Series: The Z-score of the input data, which can be used to assess price deviations.
    """
    return (data - data.mean()) / data.std()


def generate_mean_reversion_signals(
    data: pd.Series, entry_threshold: float = 1.0, exit_threshold: float = 0.0
) -> pd.Series:
    """
    Generate trading signals based on a mean reversion strategy.

    This strategy assumes that prices will revert to their mean over time.
    A buy signal is generated when the price is significantly below the mean (indicating it may be undervalued),
    and a sell signal is generated when the price is significantly above the mean (indicating it may be overvalued).

    Args:
        data (pd.Series): The input price data series (e.g., closing prices of a stock).
        entry_threshold (float): The Z-score threshold for entering a position (default is 1.0).
        exit_threshold (float): The Z-score threshold for exiting a position (default is 0.0).

    Returns:
        pd.Series: A series of trading signals (-1 for sell, 1 for buy, 0 for hold).
        A buy signal (1) indicates a potential long position,
        a sell signal (-1) indicates a potential short position,
        and a hold signal (0) indicates no action.
    """
    z_scores = calculate_z_score(data)
    signals = pd.Series(0, index=data.index)

    # Buy signal when Z-score is less than negative entry threshold
    signals[z_scores < -entry_threshold] = 1  # Buy signal
    # Sell signal when Z-score is greater than positive entry threshold
    signals[z_scores > entry_threshold] = -1  # Sell signal
    # Hold signal when Z-score is between the entry and exit thresholds
    signals[(z_scores >= -exit_threshold) & (z_scores <= exit_threshold)] = (
        0  # Hold signal
    )

    return signals


# Additional functions for the strategy can be added here...
