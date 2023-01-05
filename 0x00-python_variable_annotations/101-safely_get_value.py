#!/usr/bin/env python3
""" Type annotations are a way to explicitly
define the type of a variable."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    "If the key is in the dictionary, return the value,
    otherwise return the default value."

    The function is generic, meaning that it can be used
    with any type of dictionary and any type of
    key. The type of the value returned by the function is
    the same as the type of the default value

    :param dct: Mapping
    :type dct: Mapping
    :param key: The key to look up in the dictionary
    :type key: Any
    :param default: The default value to return if the key is not found
    :type default: Union[TypeVar('T'), None]
    :return: The value of the key in the dictionary, or the
    default value if the key is not in the
    dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
