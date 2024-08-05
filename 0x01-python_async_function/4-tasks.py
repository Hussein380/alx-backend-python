#!/usr/bin/env python3
'''Task 4's module.
'''

import asyncio
from typing import List

# Import the task_wait_random function from 3-tasks
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times and returns a sorted list of delays.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay for the task_wait_random.

    Returns:
        List[float]: A sorted list of delays.
    '''
    # Create and run tasks concurrently
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    # Return the sorted list of delays
    return sorted(wait_times)
