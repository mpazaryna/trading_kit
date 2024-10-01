from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd

from trading_kit.exceptions import InvalidDataError, InvalidThresholdError


def plot_line_chart(
    data: pd.Series,
    title: str = "Line Chart",
    xlabel: str = "X-axis",
    ylabel: str = "Y-axis",
    save_path: Optional[str] = None,
) -> None:
    """Plot a line chart for the given data and optionally save it to a file."""
    if not isinstance(data, pd.Series):
        raise InvalidDataError("Input data must be a pandas Series.")

    plt.figure(figsize=(10, 5))
    plt.plot(data, marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()

    if save_path:
        plt.savefig(save_path)  # Save the plot to the specified path
    else:
        plt.show()  # Show the plot if no save path is provided
