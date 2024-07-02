from typing import List
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]

# Test cases
testCases = [
    [[1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]],
    [[1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 4, 5, 6, 7]],
    [[1, 2, 3, 4, 5, 6, 7], 100, [6, 7, 1, 2, 3, 4, 5]],
    [[-1, -100, 3, 99], 2, [3, 99, -1, -100]],
    [[1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7]]
]

solution = Solution()

for i, (nums, k, expected_result) in enumerate(testCases, 1):
    solution.rotate(nums, k)
    print(f"Test case {i} result: {expected_result == nums}")