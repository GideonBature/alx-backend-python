#!/usr/bin/env python3
"""Duck typing - first element of a sequence
"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment the code with correct duck-typed annotations
    args:
        lst: Sequence[Any]
    return:
        Union[Any, NoneType]
    """
    if lst:
        return lst[0]
    else:
        return None
