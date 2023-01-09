#!/usr/bin/env python3
''' Measure the time it takes to execute a function '''


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time it takes to execute a function

    :param n: the number of times to call wait_random
    :type n: int
    :param max_delay: The maximum delay in seconds
    :type max_delay: int
    :return: The average time it takes to execute wait_n
    """
    import asyncio
    import time
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
