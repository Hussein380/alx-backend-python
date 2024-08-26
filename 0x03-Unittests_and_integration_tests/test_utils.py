#!/usr/bin/env python3
'''Module to test utilities in the utils file.
'''

from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    '''Test cases for the access_nested_map function.
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Test case: Simple dictionary access
        ({"a": {"b": 2}}, ("a",), {'b': 2}),  # Test case: Nested dictionary
        ({"a": {"b": 2}}, ("a", "b"), 2)  # Test case: Nested dictionary
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the correct value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),  # Test case: Key not found in empty dictionary
        ({"a": 1}, ("a", "b"), 'b')  # Test case: Key not found in nested
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that access_nested_map raises KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected JSON payload.
        """
        # Mocking requests.get to return the test_payload
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock_get = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once()  # Ensure the mocked get was called onc
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator.
    """

    def test_memoize(self):
        """Test that memoize caches results and calls the method only once.
        """
        class TestClass:
            """Class to test the memoize decorator.
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Mock the a_method to test memoization
        with patch.object(TestClass, 'a_method') as mock_method:
            test_instance = TestClass()
            test_instance.a_property()  # First call
            test_instance.a_property()  # Second call
            mock_method.assert_called_once()  # Ensure the method is called
