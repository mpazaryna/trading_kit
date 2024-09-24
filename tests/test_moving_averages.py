"""
This module contains unit tests for the moving averages calculations used in financial analysis.
It tests Simple Moving Average (SMA) and Weighted Moving Average (WMA) functions with various scenarios.
Edge cases include handling of None values for initial periods where the window size is not met.
Assumptions: The input data is a pandas Series and the window size is appropriate for the data length.
"""

import pandas as pd
import pytest

from trading_kit.indicators.moving_averages import (
    calculate_sma,
    calculate_wma,
    calculate_wma_precision,
)


def test_calculate_sma():
    """
    Test the Simple Moving Average (SMA) calculation.
    Uses a fixed set of sample data and a window size of 3.
    """
    data = pd.Series([1, 2, 3, 4, 5])
    expected = pd.Series([None, None, 2.0, 3.0, 4.0])  # SMA with window=3
    result = calculate_sma(data, window=3)
    pd.testing.assert_series_equal(result, expected)


def test_calculate_wma_real_world():
    """
    Test the Weighted Moving Average (WMA) calculation using real-world financial data.

    This test simulates a scenario where we analyze the closing prices of a stock over a
    period of time. The WMA is calculated using a window of 3 days, which gives more weight
    to the most recent prices. This is a common practice in financial analysis to smooth
    out price data and identify trends.

    The expected values are derived from the following closing prices:
    - Day 1: 100
    - Day 2: 102
    - Day 3: 104
    - Day 4: 106
    - Day 5: 108

    The WMA for these prices with a window of 3 is calculated as follows:
    - WMA(100, 102, 104) = (100*1 + 102*2 + 104*3) / (1 + 2 + 3) = 102.67
    - WMA(102, 104, 106) = (102*1 + 104*2 + 106*3) / (1 + 2 + 3) = 104.67
    - WMA(104, 106, 108) = (104*1 + 106*2 + 108*3) / (1 + 2 + 3) = 106.67

    The test checks if the calculated WMA matches the expected values.
    """
    data = pd.Series([100, 102, 104, 106, 108])
    expected = pd.Series([None, None, 102.67, 104.67, 106.67])  # WMA with window=3
    result = calculate_wma(data, window=3).round(2)
    print("Calculated WMA:", result)
    print("Expected WMA:", expected)
    pd.testing.assert_series_equal(result, expected)


def test_calculate_wma():
    """
    Test the Weighted Moving Average (WMA) calculation.
    Uses a fixed set of sample data and a window size of 3.
    """
    data = pd.Series([1, 2, 3, 4, 5])
    expected = pd.Series(
        [None, None, 2.3333333333333335, 3.3333333333333335, 4.333333333333333]
    )  # WMA with window=3
    result = calculate_wma(data, window=3)
    pd.testing.assert_series_equal(result, expected)


@pytest.mark.parametrize(
    "precision, expected",
    [
        (2, pd.Series([None, None, 102.67, 104.67, 106.67])),
        (4, pd.Series([None, None, 102.6667, 104.6667, 106.6667])),
        (6, pd.Series([None, None, 102.666667, 104.666667, 106.666667])),
    ],
)
def test_calculate_wma_precision(precision, expected):
    """
    Test the Weighted Moving Average (WMA) calculation with variable precision.

    This parametrized test verifies the correct functionality of the
    calculate_wma_precision function for different levels of precision. It uses
    a fixed set of sample data and a window size of 3, testing the function's
    output against pre-calculated expected values at various precision levels.

    The test cases cover the following scenarios:
    1. Standard 2-decimal precision (common for most stock price analyses)
    2. 4-decimal precision (useful for forex or more precise calculations)
    3. 6-decimal precision (for high-precision requirements or testing limits)

    Parameters:
    -----------
    precision : int
        The number of decimal places to round the WMA results to.
    expected : pd.Series
        The expected WMA values for the given precision level.

    Test Data:
    ----------
    The test uses the following sample price data:
    [100, 102, 104, 106, 108]

    This simulates 5 days of closing prices for a hypothetical stock.

    Calculation Method:
    -------------------
    The WMA for these prices with a window of 3 is calculated as follows:
    - WMA(100, 102, 104) = (100*1 + 102*2 + 104*3) / (1 + 2 + 3) = 102.6666...
    - WMA(102, 104, 106) = (102*1 + 104*2 + 106*3) / (1 + 2 + 3) = 104.6666...
    - WMA(104, 106, 108) = (104*1 + 106*2 + 108*3) / (1 + 2 + 3) = 106.6666...

    The expected values are then rounded to the specified precision.

    Assertions:
    -----------
    The test uses pandas' assert_series_equal to ensure that the calculated
    WMA matches the expected values at the specified precision level.

    Notes:
    ------
    - The first two values in the expected series are None, as a 3-day WMA
      cannot be calculated for the first two days.
    - This test helps ensure that the calculate_wma_precision function
      correctly handles different precision requirements, which is crucial
      for various financial applications and trading strategies.
    """
    data = pd.Series([100, 102, 104, 106, 108])
    result = calculate_wma_precision(data, window=3, precision=precision)
    pd.testing.assert_series_equal(result, expected, check_names=False)
    print(f"Test passed for precision {precision}")
    print(f"Calculated WMA: {result}")
    print(f"Expected WMA: {expected}\n")
