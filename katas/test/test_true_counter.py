import unittest
from katas.true_counter import count_true_values


class Test_true_counter(unittest.TestCase):
    def test_count_true_values(self):
        
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)
        self.assertEqual(count_true_values([False, False, False,1,False, False]), 1)

