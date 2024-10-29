import unittest
from main import Solution

class RomanToIntegerTest(unittest.TestCase):
    def test_III(self):
        self.assertEqual(Solution.toInteger("III"), 3)
    def test_LVIII(self):
        self.assertEqual(Solution.toInteger("LVIII"), 58)
    def test_IV(self):
        self.assertEqual(Solution.toInteger("IV"), 4)
    def test_XC(self):
        self.assertEqual(Solution.toInteger("XC"), 90)
    def test_XCV(self):
        self.assertEqual(Solution.toInteger("XCV"), 95)
    def test_DCXXI(self):
        self.assertEqual(Solution.toInteger("DCXXI"), 621)
    def test_MCXMCIV(self):
        self.assertEqual(Solution.toInteger("MCMXCIV"), 1994)


if __name__ == "__name__":
    unittest.main()
