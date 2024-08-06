#!/usr/bin/env python3
'''
async_comprehensipon  module
This module contains the asycn_comp[rehension coroutines that collects random
numbers from async_generator
'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    coroutine that collects 10 random numbers using async comprehension
    over async_generator, then returns the 10 random numbers

    """
    return [i async for i in async_generator()]
