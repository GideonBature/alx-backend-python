#!/usr/bin/env python3
"""complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float, ...]) -> float:
    """type annotated function
    args:
        input_list: list[float]
    return:
        float
    """
    return sum(input_list)

