#!/usr/bin/env python3
""" Module for testing client """

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ Class for Testing Github Org Client """

    @parameterized.expand([
        ('google'),  # Test case with organization name 'google'
        ('abc')  # Test case with organization name 'abc'
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value"""
        # Create an instance of GithubOrgClient with the given input
        test_class = GithubOrgClient(input)
        # Call the org method which is expected to use get_json
        test_class.org()
        # Check that get_json was called once with the correct URL
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        # Mock the 'org' property of GithubOrgClient
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}  # Mock payload
            mock.return_value = payload
            # Create an instance of GithubOrgClient
            test_class = GithubOrgClient('test')
            # Get the _public_repos_url property
            result = test_class._public_repos_url
            # Verify the result matches the expected URL
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen paylod
        Test that the mocked property and the mocked get_json was called once.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload  # Set return value for get_j

        # Mock the _public_repos_url property
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"  # Mock URL
            # Create an instance of GithubOrgClient
            test_class = GithubOrgClient('test')
            # Call public_repos to get the list of repos
            result = test_class.public_repos()

            # Generate the list of repo names from the mock payload
            check = [i["name"] for i in json_payload]
            # Verify the result matches the expected repo names
            self.assertEqual(result, check)

            # Check that the mocked properties were called once
            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Unit test for GithubOrgClient.has_license"""
        # Check if the repo has the specified license
        result = GithubOrgClient.has_license(repo, license_key)
        # Verify that the result matches the expected value
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD  # Use TEST_PAYLOAD fixture for parameterized testing
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration test of fixtures """

    @classmethod
    def setUpClass(cls):
        """Class method called before tests in the class are run"""
        # Mock HTTP responses for the get_json calls
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """Integration test: public repos"""
        test_class = GithubOrgClient("google")

        # Verify that the org method returns the expected payload
        self.assertEqual(test_class.org, self.org_payload)
        # Verify that repos_payload returns the expected payload
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        # Verify that public_repos returns the expected list of repos
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        # Verify that public_repos with an invalid license returns an empty
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        # Check that the mocked requests.get was called
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for public repos with License"""
        test_class = GithubOrgClient("google")

        # Verify that public_repos returns the expected list of repos
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        # Verify that public_repos with an invalid license returns an empty
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        # Verify that public_repos with the "apache-2.0" license returns the
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
        # Check that the mocked requests.get was called
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Class method called after tests in the class have run"""
        cls.get_patcher.stop()
