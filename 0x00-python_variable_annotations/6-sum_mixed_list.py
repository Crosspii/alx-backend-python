#!/usr/bin/env python3
''' Module of task 6 '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Returns the sum of a mixed list of ints and floats '''
    return float(sum(mxd_lst))
