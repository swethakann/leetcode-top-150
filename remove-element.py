from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r, wr = 0, 0
        m = len(nums)

        while r < m:
            while r < m and nums[r] == val:
                r += 1
            if r < m and nums[r] != val:
                nums[wr] = nums[r]
                wr += 1
            r += 1
        return wr

# Test cases
testCases = [
    [[3, 2, 2, 3], 3, [2, 2]],
    [[0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]],
    [[3, 3, 3, 3], 3, []],
    [[3], 3, []],
    [[5], 3, [5]]
]

solution = Solution()

for i, (nums, val, expected_result) in enumerate(testCases, 1):
    print(f"Test case {i} result: {expected_result == nums[0:solution.removeElement(nums, val)]}")