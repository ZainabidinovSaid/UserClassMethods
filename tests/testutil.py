import unittest
from user_util import UserUtil
from user_service import UserService
from usercl import User
from datetime import datetime
import string

class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertEqual(len(user_id), 9)
        self.assertTrue(user_id[:2].isdigit())  # First two should be digits (year part)
        self.assertTrue(user_id[2:].isdigit())  # Rest should be numeric

    def test_generate_password(self):
        password = UserUtil.generate_password(10)
        self.assertEqual(len(password), 10)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

        with self.assertRaises(ValueError):
            UserUtil.generate_password(5)  # Should raise ValueError for length < 8

    def test_is_strong_password(self):
        self.assertTrue(UserUtil.is_strong_password("A1@bcdef"))  # Strong password
        self.assertFalse(UserUtil.is_strong_password("abcdefg"))  # No number, no uppercase, no special char
        self.assertFalse(UserUtil.is_strong_password("12345678"))  # No letters, only digits
        self.assertFalse(UserUtil.is_strong_password("ABCDEFGH"))  # No lowercase, no numbers
        self.assertFalse(UserUtil.is_strong_password("abcdefgh"))  # No uppercase, no numbers
        self.assertFalse(UserUtil.is_strong_password("A1bcdefg"))  # Missing special char

    def test_generate_email(self):
        email = UserUtil.generate_email("John", "Doe")
        self.assertEqual(email, "john.doe@gmail.com")
        email = UserUtil.generate_email("Alice", "Smith", "yahoo.com")
        self.assertEqual(email, "alice.smith@yahoo.com")
        email = UserUtil.generate_email("Anna Maria", "Brown")
        self.assertEqual(email, "anna_maria.brown@gmail.com")

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@gmail.com"))
        self.assertFalse(UserUtil.validate_email("johndoe@gmail"))  # No dot in domain
        self.assertFalse(UserUtil.validate_email("john.doe@gmailcom"))  # No dot
        self.assertFalse(UserUtil.validate_email("johndoe.gmail.com"))  # No @
        self.assertFalse(UserUtil.validate_email("john@doe@gmail.com"))  # Multiple @
        self.assertFalse(UserUtil.validate_email("john.doe@com"))  # No domain part


if __name__ == "__main__":
    unittest.main()
