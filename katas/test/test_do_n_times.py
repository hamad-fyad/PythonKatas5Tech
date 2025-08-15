import unittest
from katas.do_n_times import do_n_times , say_hello, print_message



class Test_do_n_times(unittest.TestCase):
    def test_do_n_times(self):
        self.assertEqual(do_n_times(say_hello, 3), ["Hello!", "Hello!", "Hello!"])
        self.assertEqual(do_n_times(print_message, 5), ["Python is fun!", "Python is fun!", "Python is fun!", "Python is fun!", "Python is fun!"])

        
