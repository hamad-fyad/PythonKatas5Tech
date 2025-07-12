import unittest
from katas.sum_of_digits import sum_of_digits


class Test_sum_of_digits(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits("abc123"), 6)
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)
        self.assertEqual(sum_of_digits("No digits here!"), 0)
        self.assertEqual(sum_of_digits("abc00000001"), 1)
        self.assertEqual(sum_of_digits("52 cats and 2 dogs"), 9)
  
   
