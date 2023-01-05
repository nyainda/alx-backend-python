#!/usr/bin/env python3
""" Type annotations are a way to explicitly"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    "Given a key and a value, return a tuple of the key and the value squared."
    :param k: str
    :type k: str
    :param v: The value to be squared
    :type v: Union[int, float]
    :return: A tuple of the key and the value squared.
    """
    return (k, v * v)
