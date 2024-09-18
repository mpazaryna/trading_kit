from typing import Tuple

import pandas as pd


def detect_support_resistance(data: pd.DataFrame, window: int) -> Tuple[float, float]:
    """Detect support and resistance levels."""
    support = data["low"].iloc[-window:].min()  # Minimum of the last 'window' lows
    resistance = data["high"].iloc[-window:].max()  # Maximum of the last 'window' highs
    return support, resistance
