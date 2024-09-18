import matplotlib.pyplot as plt
import pandas as pd


def plot_line_chart(
    data: pd.Series,
    title: str = "Line Chart",
    xlabel: str = "X-axis",
    ylabel: str = "Y-axis",
    save_path: str = None,
) -> None:
    """Plot a line chart for the given data and optionally save it to a file."""
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
