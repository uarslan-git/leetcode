import unittest
from main import Solution
from main import ListNode

class TwoSumTest(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def linkedListEqual(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1=l1.next
            l2=l2.next
        return l1 is None and l2 is None

    def testShouldReturn807(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        
        expectedResult = ListNode(7,ListNode(0,ListNode(8)))
        result = Solution.addTwoNumbers(self,l1=l1,l2=l2)

        self.assertTrue(self.linkedListEqual(expectedResult, result))

if __name__ == "__name":
    unittest.main()
