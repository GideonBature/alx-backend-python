#!/usr/bin/env python3
"""0. Parameterize a unit test
1. Parameterize a unit test
2. Mock HTTP calls
3. Parameterize and patch
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestAccessNestedMap(unittest.TestCase):
    """first unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test accessing a value in a nested map with a key path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test accessing a value in a nested map with a key path.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """second unit test for utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://example.com/1", {"payload": False}),
    ])
    def test_get_json(self, url, expected):
        """Test get_json
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = expected
            self.assertEqual(get_json(url), expected)


class TestMemoize(unittest.TestCase):
    """third unit test for utils.memoize
    """
    def test_memoize(self):
        """Test memoize
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()
