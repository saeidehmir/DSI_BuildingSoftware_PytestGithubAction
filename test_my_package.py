# tests.py
import unittest
from TopGithubRepos.get_top_repos import get_top_repos

class TestGetTopRepos(unittest.TestCase):

    def test_get_top_repos_returns_data(self):
        """Test that the function returns a list of tuples with the correct length."""
        N = 5
        result = get_top_repos(N, test=True)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), N)


if __name__ == '__main__':
    unittest.main()