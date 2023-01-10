#!/usr/bin/env python3
"""1. Async Comprehensions """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    "Return a list of floats, where each float is the result
    of awaiting an element from the
    async_generator."

    The above function is equivalent to the following:
    :return: A list of floats.
    """
    return [element async for element in async_generator()]
