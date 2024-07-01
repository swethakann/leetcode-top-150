from typing import List
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of the 
elements should be kept the same. Return the number of unique elements in nums.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r, wr = 1, 1
        n = len(nums)

        while r < n:
            if nums[r-1] != nums[r]:
                nums[wr] = nums[r]
                wr += 1
            r +=1

        return wr

# Test cases
testCases = [
    [[1, 1, 2], 2],
    [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5],
    [[0], 1],
    [[0, 0], 1],
    [[0, 1], 2]
]

solution = Solution()

for i, (nums, expected_result) in enumerate(testCases, 1):
    print(f"Test case {i} result: {expected_result == solution.removeDuplicates(nums)}")