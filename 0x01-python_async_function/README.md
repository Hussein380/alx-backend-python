---

# Python Async Project

## Overview

This project involves implementing asynchronous programming using Python's `asyncio` library. The project consists of several tasks that demonstrate the use of asynchronous coroutines, tasks, and runtime measurements. 

## Learning Objectives

By the end of this project, you should be able to:
- Understand and use `async` and `await` syntax.
- Execute asynchronous programs with `asyncio`.
- Run concurrent coroutines.
- Create and manage `asyncio` tasks.
- Utilize the `random` module in asynchronous tasks.

## Tasks

### 0. The Basics of Async

- **File**: `0-basic_async_syntax.py`
- **Description**: Write an asynchronous coroutine named `wait_random` that takes an integer argument `max_delay` (with a default value of 10). It waits for a random delay between 0 and `max_delay` seconds and returns the delay.
- **Usage**:
  ```python
  import asyncio
  from 0_basic_async_syntax import wait_random
  
  print(asyncio.run(wait_random()))
  print(asyncio.run(wait_random(5)))
  print(asyncio.run(wait_random(15)))
  ```

### 1. Let's Execute Multiple Coroutines at the Same Time with Async

- **File**: `1-concurrent_coroutines.py`
- **Description**: Import `wait_random` and write an asynchronous coroutine named `wait_n` that spawns `wait_random` `n` times with the specified `max_delay`. The coroutine should return the list of all delays in ascending order.
- **Usage**:
  ```python
  import asyncio
  from 1_concurrent_coroutines import wait_n
  
  print(asyncio.run(wait_n(5, 5)))
  print(asyncio.run(wait_n(10, 7)))
  print(asyncio.run(wait_n(10, 0)))
  ```

### 2. Measure the Runtime

- **File**: `2-measure_runtime.py`
- **Description**: Import `wait_n` and create a function named `measure_time` that measures the total execution time for `wait_n(n, max_delay)`. The function should return the average time per task.
- **Usage**:
  ```python
  import asyncio
  from 2_measure_runtime import measure_time
  
  n = 5
  max_delay = 9
  
  print(measure_time(n, max_delay))
  ```

### 3. Tasks

- **File**: `3-tasks.py`
- **Description**: Import `wait_random` and write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task` object.
- **Usage**:
  ```python
  import asyncio
  from 3_tasks import task_wait_random
  
  async def test(max_delay: int) -> float:
      task = task_wait_random(max_delay)
      await task
      print(task.__class__)
  
  asyncio.run(test(5))
  ```

### 4. Tasks

- **File**: `4-tasks.py`
- **Description**: Create a function `task_wait_n` that is similar to `wait_n`, but uses `task_wait_random` instead. It should return the list of delays in ascending order.
- **Usage**:
  ```python
  import asyncio
  from 4_tasks import task_wait_n
  
  n = 5
  max_delay = 6
  print(asyncio.run(task_wait_n(n, max_delay)))
  ```

## Requirements

- Python 3.7
- All files must end with a newline.
- Files should be executable.
- Code should follow `pycodestyle` standards.
- Documentation for modules and functions is mandatory.

## Running the Code

1. Ensure Python 3.7 is installed on your system.
2. Make each Python file executable:
   ```bash
   chmod +x filename.py
   ```
3. Run the main files for each task as shown in the usage sections.

---
