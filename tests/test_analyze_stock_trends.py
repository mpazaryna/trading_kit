import numpy as np
import pandas as pd
import pytest

from trading_kit.strategies.analyze_stock_trends import (
    analyze_stock_trends,
    analyze_stock_trends_from_json,
)


def test_analyze_stock_trends():
    """
    Test the analyze_stock_trends function with sample data.

    This test demonstrates how to use the analyze_stock_trends function
    in a real-world scenario. It generates sample price data, calls the
    function, and performs basic checks on the results.
    """
    # Generate sample price data
    np.random.seed(42)  # for reproducibility
    dates = pd.date_range(start="2023-01-01", periods=100, freq="D")
    prices = pd.Series(np.random.randn(100).cumsum() + 100, index=dates)

    # Call the function
    short_wma, long_wma, signals = analyze_stock_trends(prices)

    # Perform checks
    assert len(short_wma) == len(prices), "Short WMA length should match price data"
    assert len(long_wma) == len(prices), "Long WMA length should match price data"
    assert len(signals) == len(prices), "Signals length should match price data"

    assert short_wma.index.equals(
        prices.index
    ), "Short WMA index should match price data index"
    assert long_wma.index.equals(
        prices.index
    ), "Long WMA index should match price data index"
    assert signals.index.equals(
        prices.index
    ), "Signals index should match price data index"

    assert np.isnan(signals.iloc[:29]).all(), "First 29 signal values should be NaN"
    assert set(signals.dropna().unique()) <= {
        -1,
        0,
        1,
    }, "Signals should only contain -1, 0, or 1"

    print("Test passed successfully!")
    print("\nSample results:")
    print("Short-term WMA (first 5):")
    print(short_wma.head())
    print("\nLong-term WMA (first 5):")
    print(long_wma.head())
    print("\nSignals summary:")
    print(signals.value_counts())


def generate_realistic_stock_data(
    start_date: str, end_date: str, initial_price: float, volatility: float
) -> pd.Series:
    """
    Generate realistic daily stock price data.

    Parameters:
    -----------
    start_date : str
        The start date for the data in 'YYYY-MM-DD' format.
    end_date : str
        The end date for the data in 'YYYY-MM-DD' format.
    initial_price : float
        The initial stock price.
    volatility : float
        The volatility of the stock price (standard deviation of daily returns).

    Returns:
    --------
    pd.Series
        A pandas Series with DatetimeIndex representing daily closing prices.
    """
    date_range = pd.date_range(
        start=start_date, end=end_date, freq="B"
    )  # 'B' for business days
    num_days = len(date_range)

    # Generate random returns
    returns = np.random.normal(loc=0, scale=volatility, size=num_days)

    # Calculate cumulative returns
    cumulative_returns = np.exp(np.cumsum(returns))

    # Generate prices
    prices = initial_price * cumulative_returns

    return pd.Series(prices, index=date_range, name="Close")


def test_acme_stock_trend_analysis():
    """
    Test the analyze_stock_trends function with realistic Acme Corp stock data.

    This test simulates a year of daily stock prices for Acme Corp and applies
    the trend analysis function to generate buy/sell signals. It then performs
    various checks on the results and prints out summary statistics.
    """
    # Generate sample data for Acme Corp
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    initial_price = 100.0  # Starting price of $100
    volatility = 0.02  # 2% daily volatility

    acme_prices = generate_realistic_stock_data(
        start_date, end_date, initial_price, volatility
    )

    # Analyze trends
    short_window = 20  # 20-day short-term WMA
    long_window = 50  # 50-day long-term WMA
    precision = 2

    short_wma, long_wma, signals = analyze_stock_trends(
        acme_prices, short_window, long_window, precision
    )

    # Perform checks
    assert len(short_wma) == len(
        acme_prices
    ), "Short WMA length should match price data"
    assert len(long_wma) == len(acme_prices), "Long WMA length should match price data"
    assert len(signals) == len(acme_prices), "Signals length should match price data"

    assert np.isnan(
        signals.iloc[: long_window - 1]
    ).all(), f"First {long_window-1} signal values should be NaN"
    assert set(signals.dropna().unique()) <= {
        -1,
        0,
        1,
    }, "Signals should only contain -1, 0, or 1"

    # Print summary statistics
    print("Acme Corp Stock Trend Analysis Summary")
    print("======================================")
    print(f"Analysis period: {start_date} to {end_date}")
    print(f"Number of trading days: {len(acme_prices)}")
    print(f"\nStock Price Summary:")
    print(acme_prices.describe().round(2))

    print(f"\nSignal Summary:")
    print(signals.value_counts().sort_index())

    print(f"\nLast 5 days of analysis:")
    last_5_days = pd.DataFrame(
        {
            "Price": acme_prices.tail(),
            "Short_WMA": short_wma.tail(),
            "Long_WMA": long_wma.tail(),
            "Signal": signals.tail(),
        }
    ).round(2)
    print(last_5_days)

    # Additional analysis
    signal_changes = signals.diff().abs().sum()
    print(f"\nNumber of trading signal changes: {signal_changes}")

    # Identify potential profitable trades (simplistic approach)
    buy_prices = acme_prices[signals.shift(1) == 1]
    sell_prices = acme_prices[signals.shift(1) == -1]
    if len(buy_prices) > 0 and len(sell_prices) > 0:
        potential_profit = (
            (sell_prices.mean() - buy_prices.mean()) / buy_prices.mean() * 100
        )
        print(f"Potential average trade profit: {potential_profit:.2f}%")
    else:
        print("Not enough buy/sell signals to calculate potential profit.")

    print("\nTest completed successfully!")
