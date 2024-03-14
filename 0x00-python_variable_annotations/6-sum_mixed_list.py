#!/usr/bin/env python3
"""Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a type annonated function
    args:
        mxd_lst: List[float, int]
    return:
        float
    """
    return float(sum(mxd_lst))
