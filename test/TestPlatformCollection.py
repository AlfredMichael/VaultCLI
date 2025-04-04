import unittest
from unittest.mock import patch

from core.user_input import collect_platform


class TestPlatformCollection(unittest.TestCase):
    @patch("builtins.input", side_effect=["securekey123", "Gmail"])
    def test_collect_platform(self, mock_input):
        platform, key = collect_platform()
        self.assertEqual(platform, "Gmail")
        self.assertEqual(key, "securekey123")
