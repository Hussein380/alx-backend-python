#!/usr/bin/env python3
'''Task 3's module.
'''

import asyncio

# Import the wait_random coroutine from the 0-basic_async_syntax module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates an asynchronous task for wait_random.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The asyncio Task for the wait_random coroutine.
    '''
    return asyncio.create_task(wait_random(max_delay))
