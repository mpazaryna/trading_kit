import pytest

from trading_kit.execution.order_types import LimitOrder, MarketOrder


def test_market_order():
    order = MarketOrder(10)
    assert order.execute() == "Executed Market Order for 10 units."


def test_limit_order():
    order = LimitOrder(5, 100.0)
    assert order.execute() == "Executed Limit Order for 5 units at $100.0."


# Additional tests can be added here...
