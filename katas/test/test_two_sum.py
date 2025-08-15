from katas.two_sum import two_sum
import unittest
class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])  # Valid case
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])  # Valid case
        self.assertEqual(two_sum([3, 3], 6), [0, 1])  # Valid case
        self.assertEqual(two_sum([1, 2, 3], 7), [])  # No valid pair
        self.assertEqual(two_sum([], 5), [])  # Empty list case
        