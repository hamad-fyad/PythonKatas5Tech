import unittest
from katas.longest_common_prefix import longest_common_prefix


class Test_longest_common_prefix(unittest.TestCase):
    def test_longest_common_prefix(self):
        
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")
        self.assertEqual(longest_common_prefix(["interspecies", "interstellar", "interstate"]), "inters")
        self.assertEqual(longest_common_prefix(["apple", "apricot", "ape"]), "ap")
        self.assertEqual(longest_common_prefix(["aepple", "asepricot", "aepe"]), "a")
        
