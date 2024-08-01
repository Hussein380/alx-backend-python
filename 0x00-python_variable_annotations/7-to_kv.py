#!/usr/bin/env python3
"""
to_kv : function that take k and v
Args:
    k: string argument
    v : float or int
Returns: tuple of k(string), v  float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> tuple[str, float]:
    return (k, float(v**2))
