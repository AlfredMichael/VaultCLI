import unittest
from unittest.mock import patch

from main import main


class TestMainApplication(unittest.TestCase):
    @patch("builtins.input", side_effect=["1", "John", "user@example.com", "securekey123", "6"])
    # Ensure the flow runs correctly with mocked inputs
    def test_main_menu(self, mock_input):
        main()
