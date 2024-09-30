# src/trading_kit/decorators.py
from functools import wraps

import pandas as pd


def dict_io(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "prices" in kwargs and isinstance(kwargs["prices"], list):
            kwargs["prices"] = pd.Series(kwargs["prices"])
        result = func(*args, **kwargs)
        return result

    return wrapper
