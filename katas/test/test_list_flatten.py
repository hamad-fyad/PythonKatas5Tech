import unittest
from katas.list_flatten import flatten_list


class Test_list_flatten(unittest.TestCase):
    def test_flatten_list(self):
       

        self.assertEqual(flatten_list([[1, 2, 3], [4, 5], [6, 7]]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(flatten_list([[1, 2, 3], [4, 5], [6, 7], [8, 9]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(flatten_list([[1, [2,[3], 3]], [4, 5], [6, 7], [8, 9], [10, 11, 12]]), [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
