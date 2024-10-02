from typing import List, Optional, Union

import matplotlib.pyplot as plt
import pandas as pd

from trading_kit.exceptions import InvalidDataError, InvalidThresholdError


def plot_line_chart(
    data: Union[List[float], List[int]],
    x_values: Optional[List[Union[float, int, str]]] = None,
    title: str = "Line Chart",
    xlabel: str = "X-axis",
    ylabel: str = "Y-axis",
    save_path: Optional[str] = None,
) -> None:
    """Plot a line chart for the given data and optionally save it to a file."""
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise InvalidDataError("Input data must be a list of numbers.")

    # Convert data to pandas Series
    if x_values is None:
        series = pd.Series(data)
    else:
        if len(x_values) != len(data):
            raise InvalidDataError("x_values must have the same length as data.")
        series = pd.Series(data, index=x_values)

    plt.figure(figsize=(10, 5))
    plt.plot(series, marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()

    if save_path:
        plt.savefig(save_path)  # Save the plot to the specified path
    else:
        plt.show()  # Show the plot if no save path is provided
