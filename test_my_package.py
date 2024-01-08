#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 22:03:04 2024

@author: saeideh
"""

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