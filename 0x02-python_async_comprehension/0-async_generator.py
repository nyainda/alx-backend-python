#!/usr/bin/env python3

""" Async Generator """

from random import uniform
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    It's a generator that yields random numbers between 0 and 10,
    with a 1 second delay between each
    number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
