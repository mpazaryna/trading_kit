def calculate_position_size(
    account_balance: float,
    risk_per_trade: float,
    entry_price: float,
    stop_loss_price: float,
) -> float:
    """
    Calculate the position size for a trade based on account balance, risk per trade, entry price, and stop loss price.

    Parameters:
    account_balance (float): The total account balance available for trading.
    risk_per_trade (float): The amount of capital to risk on a single trade (as a percentage of account balance).
    entry_price (float): The price at which the trade will be entered.
    stop_loss_price (float): The price at which the trade will be exited to limit losses.

    Returns:
    float: The position size (number of shares/contracts) to trade.

    Raises:
    ValueError: If stop_loss_price is greater than or equal to entry_price.
    """
    if stop_loss_price >= entry_price:
        raise ValueError("Stop loss price must be less than entry price.")

    risk_amount = account_balance * (risk_per_trade / 100)
    risk_per_share = entry_price - stop_loss_price
    position_size = risk_amount / risk_per_share

    return position_size
