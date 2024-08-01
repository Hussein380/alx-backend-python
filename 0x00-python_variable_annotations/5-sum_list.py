#!/usr/bin/env python3
"""
sum_list : annotated function which taakes input_list of loats as arg
Args:
    input_list  list of floats
Return: sum of float
"""

from typing import List

def sum_list(input_list: list[float]) -> float:
    return float(sum(input_list))
