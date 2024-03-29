#!/usr/bin/env python3
"""Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type annotated function
    args:
        multiplier: float
    return:
        Callable[[float], float]
    """

    def inner(x: float) -> float:
        return x * multiplier

    return inner
