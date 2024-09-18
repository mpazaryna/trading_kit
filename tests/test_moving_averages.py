import pandas as pd
import pytest

from trading_kit.indicators.moving_averages import calculate_sma


def test_calculate_sma():
    data = pd.Series([1, 2, 3, 4, 5])
    expected = pd.Series([None, None, 2.0, 3.0, 4.0])  # SMA with window=3
    result = calculate_sma(data, window=3)
    pd.testing.assert_series_equal(result, expected)
