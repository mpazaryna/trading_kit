from typing import Any, Dict

import pandas as pd


class MomentumStrategy:
    """Simple Momentum trading strategy implementation."""

    def __init__(self, data: pd.DataFrame, params: Dict[str, Any]):
        self.data = data
        self.params = params

    def generate_signals(self) -> pd.Series:
        """Generate trading signals based on momentum."""
        self.data["momentum"] = self.data["close"].diff()
        signals = self.data["momentum"].apply(
            lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
        )
        return signals.astype(int)  # Convert to int
