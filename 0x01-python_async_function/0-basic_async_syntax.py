#!/usr/bin/env python3
""" async await python  """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    It waits for a random amount of time, and then returns
    that random amount of time

    :param max_delay: The maximum delay in seconds, defaults to 10
    :type max_delay: int (optional)
    :return: A random float between 0 and max_delay
    """
    random_data = random.uniform(0, max_delay)
    await asyncio.sleep(random_data)
    return random_data
