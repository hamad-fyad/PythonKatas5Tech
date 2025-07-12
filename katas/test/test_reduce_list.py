import unittest
from katas.reduce_list import reduce_array


class Test_reduce_list(unittest.TestCase):
    def test_reduce_list(self):
        
        self.assertEqual(reduce_array([10, 15, 7, 20, 25]), [10, 5, -8, 13, 5])
        self.assertEqual(reduce_array([1, 2, 3, 4, 5]), [1, 1, 1, 1, 1])
        self.assertEqual(reduce_array([-1, -2, -3, -4, -5]), [-1, -1, -1, -1, -1])
        
