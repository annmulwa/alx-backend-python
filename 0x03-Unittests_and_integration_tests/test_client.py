#!/usr/bin/env python3
"""
Test the client.py file
"""
import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
import utils
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Implement the test_org method
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        get_patch.return_value = expected
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/"+org)

    def test_public_repos_url(self):
        """
        Unit-test GithubOrgClient._public_repos_url
        """
        expected = "www.alx.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """
        Unit-test GithubOrgClient.public_repos
        """
        geofrey = {"name": "Geofrey", "license": {"key": "a"}}
        bob = {"name": "Bob", "license": {"key": "b"}}
        anne = {"name": "Anne"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [geofrey, bob, anne]
        with patch(to_mock, PropertyMock(return_value="www.alx.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ['Geofrey', 'Bob', 'Anne'])
            self.assertEqual(x.public_repos("a"), ['Geofrey'])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.alx.com")
            y.assert_called_once_with()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
