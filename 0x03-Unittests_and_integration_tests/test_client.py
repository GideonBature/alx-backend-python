#!/usr/bin/env python3
"""4. Parameterize and patch as decorators
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """fourth unit test for client.GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns
        the correct JSON response.
        """
        url = f"https://api.github.com/orgs/{org_name}"
        expected_org = {"login": org_name, 'url': url}
        mock_get_json.return_value = expected_org

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_org)
        mock_get_json.assert_called_once_with(url)
