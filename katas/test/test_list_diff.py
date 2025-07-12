import unittest
from katas.list_diff import find_difference


class Test_list_diff(unittest.TestCase):
    def test_find_difference(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)
        self.assertEqual(find_difference([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_difference([-1, -2, -3, -4, -5]), 4)

        
