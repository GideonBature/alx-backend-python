#!/usr/bin/env python3
"""Let's duck type an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate function parameter and return value
        args:
        lst: Iterable[Sequence]
    return:
        List[Tuple[Sequence]]
    """
    return [(i, len(i)) for i in lst]
