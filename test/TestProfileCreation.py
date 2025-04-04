import unittest
from unittest.mock import patch

from core.user_input import collect_user_info_profile


class TestProfileCreation(unittest.TestCase):
    @patch("builtins.input", side_effect=["John", "invalid email", "user@example.com", "securekey123"])
    def test_profile_creation(self, mock_input):
        name, email, key = collect_user_info_profile()
        self.assertEqual(name, "John")
        self.assertEqual(email, "user@example.com")
        self.assertEqual(key, "securekey123")
