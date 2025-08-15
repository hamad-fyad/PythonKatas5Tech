from katas.find_missing_number import find_missing_number
import unittest

class TestFindMissingNumber(unittest.TestCase):
    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([3, 0, 1]), 2)  # Missing 2
        self.assertEqual(find_missing_number([0, 1, 3, 4, 5]), 2)  # Missing 2
        self.assertEqual(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)  # Missing 8
        self.assertEqual(find_missing_number([1, 2, 3, 4, 5]), 0)  # Missing 0

    def test_empty_list(self):
        self.assertEqual(find_missing_number([]), 0)  # No numbers to check

    def test_single_element(self):
        self.assertEqual(find_missing_number([0]), 1)  # Missing number is 1
        self.assertEqual(find_missing_number([1]), 0)  # Missing number is 0