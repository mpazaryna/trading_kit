# trading_kit/tests/test_mean_reversion.py

import pandas as pd
import pytest

from trading_kit.strategies.mean_reversion import generate_mean_reversion_signals


def test_generate_mean_reversion_signals():
    """
    Test the generate_mean_reversion_signals function.
    """
    # Sample data representing stock closing prices
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Generate signals
    signals = generate_mean_reversion_signals(
        data, entry_threshold=1.0, exit_threshold=0.0
    )

    # Check expected signals
    expected_signals = pd.Series([1, 1, 0, 0, 0, 0, 0, 0, -1, -1], index=data.index)

    pd.testing.assert_series_equal(signals, expected_signals)


# Additional tests can be added here...
