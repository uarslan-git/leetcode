import unittest
from main import Solution

class RomanToIntegerTest(unittest.TestCase):
    def test_III(self):
        self.assertEqual(Solution.toInteger("III"), 3)
#    def test_LVIII(self):
#        self.assertEqual(Solution.toInteger("LVIII"), 58)
#    def test_MCXMCIV(self):
#        self.assertEqual(Solution.toInteger("MCMXCIV"), 1994)
#

if __name__ == "__name__":
    unittest.main()
