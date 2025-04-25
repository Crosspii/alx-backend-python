#!/usr/bin/env python3
"""
Module for task 10
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it is not empty, otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
