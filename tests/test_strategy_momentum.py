import pandas as pd
import pytest

from trading_kit.strategies.momentum import MomentumStrategy


def test_generate_signals():
    data = pd.DataFrame({"close": [1, 2, 3, 2, 5, 4]})
    params = {}
    strategy = MomentumStrategy(data, params)
    expected_signals = pd.Series([0, 1, 1, -1, 1, -1])  # Expected signals
    result = strategy.generate_signals()
    result.name = None  # Remove the name from the result for comparison
    pd.testing.assert_series_equal(
        result.reset_index(drop=True), expected_signals
    )  # Reset index for comparison
