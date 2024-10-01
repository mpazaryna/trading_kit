from typing import List, Tuple

import pandas as pd


def detect_support_resistance(
    highs: List[float], lows: List[float], window: int
) -> Tuple[float, float]:
    """Detect support and resistance levels."""
    if not highs or not lows:
        raise ValueError("Highs and lows lists cannot be empty.")
    if len(highs) < window or len(lows) < window:
        raise ValueError(
            "Highs and lows lists must be at least as long as the window size."
        )
    if window <= 0:
        raise ValueError("Window size must be a positive integer.")

    support = min(lows[-window:])  # Minimum of the last 'window' lows
    resistance = max(highs[-window:])  # Maximum of the last 'window' highs
    return support, resistance
