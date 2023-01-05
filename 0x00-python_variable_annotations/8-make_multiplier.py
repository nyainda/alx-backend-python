#!/usr/bin/env python3
"""
Type annotations are a way to explicitly
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    `make_multiplier` takes a float and returns a function
    that takes a float and returns a float

    :param multiplier: float - the multiplier to use
    :type multiplier: float
    :return: A function object
    """
    def multiply(x: float) -> float:
        """
        `multiply` takes a float and returns a float

        :param x: float - the input value
        :type x: float
        :return: A function object
        """
        return x * multiplier
    return multiply
