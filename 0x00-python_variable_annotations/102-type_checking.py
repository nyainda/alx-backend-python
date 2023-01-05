#!/usr/bin/env python3
""" Type annotations are a way to explicitly
define the type of a variable."""


from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    It takes a tuple and returns a list that contains each item
    in the tuple repeated a number of times
    equal to the factor argument

    :param lst: Tuple
    :type lst: Tuple
    :param factor: int = 2, defaults to 2
    :type factor: int (optional)
    :return: A list of the items in the tuple, repeated by the factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
