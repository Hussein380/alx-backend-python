#!/usr/bin/env python3
"""
sum_mixed_list: takes mixed_list mxd_list of integers and floats
Args: mxd_list
Returns: sum as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    return float(sum(mxd_lst))
