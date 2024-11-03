import unittest
from main import Solution

class TestClass(unittest.TestCase):
    def test_brackets(self):
        self.assertEqual(Solution.isValid("()"), True)

    def test_multiple(self):
        self.assertEqual(Solution.isValid("()[]{}"), True)

    def test_failingparantheses(self):
        self.assertEqual(Solution.isValid("(]"), False)

    def test_nested(self):
        self.assertEqual(Solution.isValid("([])"),  True)

    def test_failing2(self):
        self.assertEqual(Solution.isValid("([)]"),  False)


if __name__ == '__main__':
    unittest.main()
