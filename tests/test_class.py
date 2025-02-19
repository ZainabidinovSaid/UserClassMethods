import unittest
from usercl import User
from datetime import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(34, "Saidislom", "Zainabidinov", '2006-06-13', 'saidislam1233@gmail.com', '123456')

    def test_get_details(self):
        info = "User ID: 34, Name: Saidislom Zainabidinov, Email: saidislam1233@gmail.com, Birthday: 2006-06-13"
        self.assertEqual(self.user.get_details(), info)

    def test_get_age(self):
        exp_age = datetime.now().year - 2006
        self.assertEqual(self.user.get_age(), exp_age)


if __name__ == "__name__":
    unittest.main()