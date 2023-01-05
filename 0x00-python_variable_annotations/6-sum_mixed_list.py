#!/usr/bin/env python3
""" Type annotations are a way to explicitly"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    "This function takes a list of mixed numbers and
    returns the sum of those numbers."
    :param mxd_lst: Union[int, float]
    :type mxd_lst: Union[int, float]
    :return: The sum of the list.
    """
    return sum(map(float, mxd_lst))
