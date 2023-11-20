import unittest
import time
from twosum import Solution

class TestMethod(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        elapsed_time = time.time() - self.start_time
        print(f"{self._testMethodName} ran in: {elapsed_time:.2f} seconds")

    def test_one(self):
        self.assertEqual(Solution.twoSum([2,7,11,15],9), [0,1])
    
    def test_two(self):
        self.assertEqual(Solution.twoSum([3,2,4],6), [1,2])

    def test_three(self):
        self.assertEqual(Solution.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()
