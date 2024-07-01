from typing import List
"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place 
such that each unique element appears at most twice. The relative order of the elements 
should be kept the same.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 1
        r, wr = 1, 1
        m = len(nums)

        while r < m:
            if nums[r] == nums[r - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[wr] = nums[r]
                wr += 1
            r += 1

        return wr

# Test cases
testCases = [
    [[1, 1, 2], 3],
    [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 9],
    [[0], 1],
    [[0, 0], 2],
    [[0, 1], 2]
]

solution = Solution()

for i, (nums, expected_result) in enumerate(testCases, 1):
    print(f"Test case {i} result: {expected_result == solution.removeDuplicates(nums)}")