from typing import List
"""
Given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = [-1] * len(nums)
        memo[-1] = 1

        def canJumpHelper(i):
            if memo[i] != -1:
                return memo[i] == 1

            max_jump = min(i + nums[i], len(nums) - 1)

            for j in range(i + 1, max_jump + 1):
                if canJumpHelper(j):
                    memo[i] = 1
                    return True
            memo[i] = 0
            return False

        return canJumpHelper(0)

# Test cases
testCases = [
    [[2, 3, 1, 1, 4], True],
    [[3, 2, 1, 0, 4], False]
]

solution = Solution()

for i, (nums, expected_result) in enumerate(testCases, 1):
    print(f"Test case {i} result: {expected_result == solution.canJump(nums)}")