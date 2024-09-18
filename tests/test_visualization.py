import os
import tempfile
import time
from unittest.mock import patch

import matplotlib.pyplot as plt  # Import plt here
import pandas as pd
import pytest

from trading_kit.utils.visualization import plot_line_chart


def test_plot_line_chart(monkeypatch):
    """Test the plot_line_chart function."""
    # Create sample data
    data = pd.Series([1, 2, 3, 4, 5])

    # Mock plt.show to prevent the plot from displaying during the test
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    # Call the function
    plot_line_chart(data, title="Test Chart", xlabel="Index", ylabel="Values")


def test_plot_line_chart_save():
    """Test the plot_line_chart function and save the plot to a file."""
    # Create sample data
    data = pd.Series([1, 2, 3, 4, 5])

    # Use patch to mock plt.savefig
    with patch("matplotlib.pyplot.savefig") as mock_savefig:
        # Call the function to save the plot
        plot_line_chart(
            data,
            title="Test Chart",
            xlabel="Index",
            ylabel="Values",
            save_path="test_chart.png",
        )

        # Check if the save function was called with the correct filename
        mock_savefig.assert_called_once_with("test_chart.png")  # Example filename


def test_plot_line_chart_actual_save():
    """Test the plot_line_chart function and actually save the plot to /tmp."""
    # Create sample data
    data = pd.Series([1, 2, 3, 4, 5])

    # Define the path for the temporary file in /tmp
    temp_file_path = "tmp/test_chart_actual.png"

    # Call the function to save the plot
    plot_line_chart(
        data,
        title="Test Chart",
        xlabel="Index",
        ylabel="Values",
        save_path=temp_file_path,
    )

    # Optional: Wait a moment to ensure the file is written
    time.sleep(1)

    # Check if the file was created
    assert os.path.exists(temp_file_path)  # Check if the file exists
    print(f"Plot saved to: {temp_file_path}")  # Print the path for reference
