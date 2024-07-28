#!/usr/bin/env python3
"""
Module to test utils.py file
"""
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """
    Test that the method returns what it is supposed to
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """
        Test that the method returns what it is supposed to
        """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """
        Test that a KeyError is raised
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(TestCase):
    """
    Class for testing get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that utils.get_json returns the expected result
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)

            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    """
    Class for testing memoize decorator
    """
    def test_memoize(self):
        """
        Test memoize function
        """
        class TestClass:
            """
            Test class
            """
            def a_method(self):
                """
                Returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                Returns memoized property
                """
                return self.a_method()

        with patch.abject(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
