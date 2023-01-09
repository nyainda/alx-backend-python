#!/usr/bin/env python3
''' test file for asyncio.wait() '''

import typing
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    It returns a list of n random delays, sorted from smallest to largest

    :param n: the number of times to call wait_random
    :type n: int
    :param max_delay: The maximum delay in seconds
    :type max_delay: int
    :return: A list of floats, sorted in ascending order.
    """
    return sorted(await asyncio.gather(*[wait_random(max_delay)
                                         for i in range(n)]))
