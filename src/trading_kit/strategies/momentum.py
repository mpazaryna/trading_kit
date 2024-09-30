from typing import Any, Dict, List

import pandas as pd


class MomentumStrategy:
    """Simple Momentum trading strategy implementation."""

    def __init__(self, data: List[float], params: Dict[str, Any]):
        self.data = data
        self.params = params

    def generate_signals(self) -> List[int]:
        """Generate trading signals based on momentum."""
        momentum = [
            self.data[i] - self.data[i - 1] if i > 0 else 0
            for i in range(len(self.data))
        ]
        signals = [1 if x > 0 else (-1 if x < 0 else 0) for x in momentum]
        return signals
