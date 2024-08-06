#!/usr/bin/env python3
'''
asycn_generator module
This module explain the async_generator coroutines that yield random
number
'''

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    coroutines that yield a random number betweeen 0 and 10, ten times
    Each iteration waits for1 second before it yields the number

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
