#!/usr/bin/env python3
""" Type annotations are a way to explicitly"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    It takes a list of sequences and returns a list of tuples,
    where each tuple contains a sequence and
    its length

    :param lst: Iterable[Sequence]
    :type lst: Iterable[Sequence]
    :return: A list of tuples, where each tuple contains the element and
    its length.
    """
    return [(i, len(i)) for i in lst]
