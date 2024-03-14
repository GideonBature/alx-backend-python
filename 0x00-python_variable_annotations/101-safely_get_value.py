#!/usr/bin/env python3
"""More involved type annotations
"""
from typing import Mapping, Any, Union, TypeVar, Optional
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """add type annotations to the function
    args:
        dct: Mapping
        key: Any
        default: Union
    return:
        Union: Any
    """
    if key in dct:
        return dct[key]
    else:
        return default
