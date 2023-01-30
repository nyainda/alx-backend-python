#!/usr/bin/env python3

"""Unittest class for utils.py"""

from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    the test access nested map
    test cases class.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Assert the output is equal to the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Assert the output is equal to the expected result.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        """
        Assert the output is equal to the expected result.
        """
        with patch('requests.get') as executed_function:
            executed_function.return_value.json.return_value = expected
            response = get_json(url)
            self.assertEqual(response, expected)
            executed_function.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Class for testing memoize decorator. """

    def test_memoize(self):
        """ Test memoize decorator. """
        class TestClass:
            """ temporal class for testing memoize decorator. """

            def a_method(self):
                """ a method for testing memoize decorator. """
                return 42

            @memoize
            def a_property(self):
                """ property for testing memoize decorator. """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked_fn:
            test_class = TestClass()
            returned = test_class.a_property
            self.assertEqual(returned, 42)
            mocked_fn.assert_called_once()


if __name__ == '__main__':
    unittest.main()
