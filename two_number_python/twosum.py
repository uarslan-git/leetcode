from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        matchingNumbers = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[i]+nums[j] == target:
                    matchingNumbers.append(i)
                    matchingNumbers.append(j)
                    return matchingNumbers
        return matchingNumbers
