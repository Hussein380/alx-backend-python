#!/usr/bin/env python3
'''Task 2's module.
'''

import asyncio
import time

# Importing the wait_n coroutine from the previous module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: The average time per coroutine in seconds.
    '''
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Execute the wait_n coroutine
    return (time.time() - start_time) / n
