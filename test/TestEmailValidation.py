import unittest

from core.user_input import validate_email


class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(validate_email("user@example.com"))
        self.assertTrue(validate_email("user.name@domain.co"))

    def test_invalid_email(self):
        self.assertFalse(validate_email("userexample.com"))
        self.assertFalse(validate_email("user@.com"))
        self.assertFalse(validate_email("@example.com"))
