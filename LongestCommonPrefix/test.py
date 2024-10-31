import unittest
from main import Solution

class LongestCommonPrefixTest(unittest.TestCase):
    def test_fl(self):
        strs = ["flower","flow","flight"]
        self.assertEqual(Solution.longestCommonPrefix(strs), "fl")
    def test_empty(self):
        strs = ["dog","racecar","car"]
        self.assertEqual(Solution.longestCommonPrefix(strs), "")


if __name__ == "__name__":
    unittest.main()
