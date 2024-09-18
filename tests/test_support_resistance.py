import pandas as pd
import pytest

from trading_kit.patterns.support_resistance import detect_support_resistance


def test_detect_support_resistance():
    data = pd.DataFrame({"high": [1, 2, 3, 4, 5], "low": [0, 1, 2, 3, 4]})
    expected_support = 2.0  # Minimum of the last 3 lows: [2, 3, 4]
    expected_resistance = 5.0  # Maximum of the last 3 highs: [3, 4, 5]
    result = detect_support_resistance(data, window=3)
    assert result == (expected_support, expected_resistance)
