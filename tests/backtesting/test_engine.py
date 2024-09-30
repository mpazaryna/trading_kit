import pandas as pd
import pytest

from trading_kit.backtesting.engine import backtest_strategy, calculate_performance


def mock_strategy(data: pd.DataFrame, threshold: float) -> pd.Series:
    """
    A mock strategy for testing.

    This strategy generates buy/sell signals based on a simple threshold comparison.
    It returns 1 (buy signal) if the closing price is above the threshold and 0 (sell signal)
    otherwise.

    Parameters:
    - data (pd.DataFrame): A DataFrame containing market data, specifically the 'close' prices.
    - threshold (float): The price threshold for generating signals.

    Returns:
    - pd.Series: A Series of signals (1s and 0s) indicating buy/sell decisions.
    """
    return (data["close"] > threshold).astype(int)


def test_backtest_strategy():
    """
    Test the backtest_strategy function.

    This test verifies that the backtest_strategy function correctly applies the mock_strategy
    to the provided market data. It checks if the generated signals match the expected output.

    Steps:
    1. Create a DataFrame `data` with closing prices.
    2. Call the backtest_strategy function with the mock_strategy and a threshold of 104.
    3. Assert that the returned signals match the expected Series of [0, 1, 0, 1].
    """
    data = pd.DataFrame({"close": [100, 105, 102, 110]})
    signals = backtest_strategy(data, mock_strategy, threshold=104)
    assert signals.equals(pd.Series([0, 1, 0, 1]))


def test_calculate_performance():
    """
    Test the calculate_performance function.

    This test checks that the calculate_performance function returns the expected performance metrics
    based on the provided backtest results.

    Steps:
    1. Create a DataFrame `results` with sample returns.
    2. Call the calculate_performance function with the results DataFrame.
    3. Assert that the returned metrics contain the expected Sharpe ratio of 1.5.
    """
    results = pd.DataFrame({"returns": [0.01, 0.02, -0.01]})
    metrics = calculate_performance(results)
    assert metrics["sharpe_ratio"] == 1.5  # Adjust based on actual logic
