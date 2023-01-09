#!/usr/bin/env python3
''' test file for asyncio.wait() '''

import typing
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    It creates a list of `n` tasks, each of which waits for a
    random amount of time between 0 and
    `max_delay` seconds, and then returns a list of the times
    that each task waited

    :param n: the number of tasks to run
    :type n: int
    :param max_delay: the maximum delay in seconds for each task
    :type max_delay: int
    :return: A list of floats, sorted in ascending order.
    """
    list_got = [await task_wait_random(max_delay) for delay in range(n)]
    return sorted(list_got)
