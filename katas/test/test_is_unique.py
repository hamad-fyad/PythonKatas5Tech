import unittest
from katas.is_unique_str import is_unique


class   TestIsUnique(unittest.TestCase):
    def test_is_unique_empty_str(self):
        
        self.assertEqual(is_unique(" "), True)
    def test_is_unique(self):
        
        self.assertEqual(is_unique("abc"), True)

    def test_is_unique_with_spaces(self):
        
        self.assertEqual(is_unique("a b c"), False)
