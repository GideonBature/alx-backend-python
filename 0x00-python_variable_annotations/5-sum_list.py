#!/usr/bin/env python3
"""complex types - list of floats
"""


def sum_list(input_list: list[float, ...]) -> float:
    """type annotated function
    args:
        input_list: list[float]
    return:
        float
    """
    return sum(input_list)

