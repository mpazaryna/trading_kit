from typing import List, Tuple

import pandas as pd


def detect_support_resistance(
    highs: List[float], lows: List[float], window: int
) -> Tuple[float, float]:
    """Detect support and resistance levels."""
    support = min(lows[-window:])  # Minimum of the last 'window' lows
    resistance = max(highs[-window:])  # Maximum of the last 'window' highs
    return support, resistance
