import unittest


class LoginTest(unittest.TestCase):
    def test_SignUpByEmail(self):
        print("This is login by email test")
        self.assertTrue(True)

    def test_SignUpByFacebook(self):
        print("This is login by Facebook test")
        self.assertTrue(True)

    def test_SignUpByTwitter(self):
        print("This is login by Twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
