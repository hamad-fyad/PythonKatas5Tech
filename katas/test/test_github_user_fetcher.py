from requests import RequestException
from katas.github_user_fetcher import fetch_github_user, get_user_repositories_count
import unittest
from unittest.mock import patch, MagicMock

class TestGitHubUserFetcher(unittest.TestCase):
    @patch('katas.github_user_fetcher.requests.get')
    def test_fetch_github_user_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'login': 'octocat',
            'name': 'The Octocat',
            'public_repos': 8,
            'followers': 9999
        }
        mock_get.return_value = mock_response
        
        user_info = fetch_github_user("octocat")
        self.assertIsNotNone(user_info)
        self.assertEqual(user_info['login'], 'octocat')
        self.assertEqual(user_info['name'], 'The Octocat')
        self.assertEqual(user_info['public_repos'], 8)
        self.assertEqual(user_info['followers'], 9999)

    @patch('katas.github_user_fetcher.requests.get')
    def test_fetch_github_user_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        user_info = fetch_github_user("nonexistentuser")
        self.assertIsNone(user_info)

    @patch('katas.github_user_fetcher.requests.get')
    def test_fetch_github_user_api_error(self, mock_get):
        mock_get.side_effect = RequestException()
        
        user_info = fetch_github_user("anyuser")
        self.assertIsNone(user_info)

    @patch('katas.github_user_fetcher.fetch_github_user')
    def test_get_user_repositories_count(self, mock_fetch):
        mock_fetch.return_value = {
            'login': 'octocat',
            'name': 'The Octocat',
            'public_repos': 8,
            'followers': 9999
        }
        
        repo_count = get_user_repositories_count("octocat")
        self.assertEqual(repo_count, 8)

        mock_fetch.return_value = None
        repo_count = get_user_repositories_count("nonexistentuser")
        self.assertEqual(repo_count, 0)

if __name__ == '__main__':
    unittest.main()