import numpy as np


def sharpe_ratio(returns: list[float], risk_free_rate: float = 0.0) -> float:
    """
    Calculate the Sharpe Ratio for a given list of returns.

    Parameters:
    - returns (list[float]): A list of returns.
    - risk_free_rate (float): The risk-free rate, default is 0.0.

    Returns:
    - float: The Sharpe Ratio.
    """
    returns_array = np.array(returns)
    excess_returns = returns_array - risk_free_rate
    mean_excess_return = np.mean(excess_returns)
    std_excess_return = np.std(excess_returns)

    if std_excess_return == 0:
        return float("nan")  # Avoid division by zero

    sharpe_ratio = mean_excess_return / std_excess_return
    return sharpe_ratio
