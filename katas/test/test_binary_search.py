import unittest
from katas.binary_search import binary_search



class Test_binary_search(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 7), 3)
        self.assertEqual(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 8), -1)
    def test_binary_search(self):
        self.assertEqual(binary_search([], 7), -1)
   

