from collections import Counter
from typing import List
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = Counter(nums)
        return max(elements.keys(), key=elements.get)

# Test cases
testCases = [
    [[3,2,3], 3],
    [[2,2,1,1,1,2,2], 2],
    [[1], 1],
    [[1, 1, 1, 1], 1],
]

solution = Solution()

for i, (nums, expected_result) in enumerate(testCases, 1):
    print(f"Test case {i} result: {expected_result == solution.majorityElement(nums)}")