#!/usr/bin/env python3
""" Type annotations are a way to explicitly
define the type of a variable."""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    "If the list is not empty, return the first element,
    otherwise return None."

    The type hinting in the above function is a bit more
    complex than the previous examples. The first
    argument is a Sequence, which is a generic type.
    The second argument is a Union of Any and None

    :param lst: Sequence[Any]
    :type lst: Sequence[Any]
    :return: The first element of the list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
