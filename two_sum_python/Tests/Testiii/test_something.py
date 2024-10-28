import unittest
import main

class TestSumFunction(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(main.sum(25,10),50)

if __name__ == '__main__':
    unittest.main()
