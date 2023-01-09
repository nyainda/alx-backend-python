#!/usr/bin/env python3
'''asyncio task '''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    It creates a task that waits for a random amount of time

    :param max_delay: The maximum amount of time to wait before returning
    :type max_delay: int
    :return: A task object.
    """
    return asyncio.create_task(wait_random(max_delay))
