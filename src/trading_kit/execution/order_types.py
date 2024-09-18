class OrderType:
    """Base class for order types."""

    def execute(self):
        raise NotImplementedError("This method should be overridden.")


class MarketOrder(OrderType):
    """Market Order implementation."""

    def __init__(self, quantity: int):
        self.quantity = quantity

    def execute(self):
        return f"Executed Market Order for {self.quantity} units."


class LimitOrder(OrderType):
    """Limit Order implementation."""

    def __init__(self, quantity: int, price: float):
        self.quantity = quantity
        self.price = price

    def execute(self):
        return f"Executed Limit Order for {self.quantity} units at ${self.price}."


# Additional order types can be added here...
