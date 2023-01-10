#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions  """
from asyncio import gather, run
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    It creates four tasks, each of which runs an async comprehension,
    and then waits for all four tasks
    to complete
    :return: Total time spent in float notation.
    """
    start = time.time()
    await gather(*[async_comprehension() for _ in range(4)])
    end = time.time()
    return end - start
