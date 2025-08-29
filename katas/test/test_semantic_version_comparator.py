from katas.semantic_version_comparator import compare_versions
import unittest

class TestSemanticVersionComparator(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(compare_versions("1.0.1","2.2.2"),-1)
        self.assertEqual(compare_versions("2.0.0","1.9.9"),1)
        self.assertEqual(compare_versions("1.0.0","1.0.0"),0)
        self.assertEqual(compare_versions("1.0","1.0.0"),0)
        self.assertEqual(compare_versions("1.0.1","1.0"),1)