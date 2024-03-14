#!/usr/bin/env python3
"""Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """type annonated function to_kv
    args:
        k: str
        v: int | float
    return:
        Tuple[int, float]
    """
    return (k, v ** 2)
