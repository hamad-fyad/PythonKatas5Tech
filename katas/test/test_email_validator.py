import unittest
from katas.email_validator import is_valid_email



class Test_email_validator(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertEqual(is_valid_email("test.21@hello.hi"), True)  # Valid email
        self.assertEqual(is_valid_email("asdasdasdas@@adsa.com"), False)  # Invalid email

   

