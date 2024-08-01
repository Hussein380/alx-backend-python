#!/usr/bin/env python3
"""
make_multiplier: type-annotated function that takes a float as an argument
Args:
    multiplier: argument that is a float
Return: function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
