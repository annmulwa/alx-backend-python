#!/usr/bin/env python3
"""
Module to test utils.py file
"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


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
