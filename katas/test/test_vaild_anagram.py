from katas.valid_anagram import is_anagram
import unittest
class TestValidAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("triangle", "integral"))
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))
        self.assertTrue(is_anagram("", ""))  # Edge case: both empty strings
        self.assertFalse(is_anagram("a", "b"))  # Edge case: single character strings
        self.assertTrue(is_anagram("a", "a"))  # Edge case: single character strings same
       