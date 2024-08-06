#!/usr/bin/env python3
"""
measure_runtime module
This module contains the measure_runtime coroutine that executes
async_comprehension four times in parallel and measures the total runtime.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
        using asyncio.gather, measures the total runtime, and returns it.


    """
    # Record start time
    start_time = time.time()

    # create a list of four asycn comprehension coroutines
    tasks = [async_comprehension() for _ in range(4)]

    # Run all tasks in parallel
    await asyncio.gather(*tasks)

    # Record the end time
    end_time = time.time()

    return end_time - start_time
