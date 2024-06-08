import unittest

from app import users, verify_password

class TestAppMethods(unittest.TestCase):

    def test_users_exists(self):
        self.assertIsNotNone(users, 'user variable is None')

    def test_users_user_exists(self):
        self.assertIsNotNone(users['user'], 'users key [user] not found')

    def test_users_user_set(self):
        self.assertEqual(users['user'], 'pass', 'users has wrong password')

    def test_verify_password_true(self):
        self.assertTrue(verify_password('user', 'pass'), 'verify wrong username or password')

    def test_verify_password_bad_username(self):
        self.assertFalse(verify_password('user1', 'pass'), 'verify wrong username')

    def test_verify_password_bad_password(self):
        self.assertFalse(verify_password('user', 'pass1'), 'verify wrong password')

if __name__ == '__main__':
    unittest.main()

