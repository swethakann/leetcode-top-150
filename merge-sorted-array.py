from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[0:] = nums2[0:]
            return

        p1, p2, wr = m - 1, n - 1, len(nums1) - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[wr] = nums1[p1]
                p1 -= 1
            else:
                nums1[wr] = nums2[p2]
                p2 -= 1
            wr -= 1

        if p2 >= 0:
            nums1[0:p2 + 1] = nums2[0:p2 + 1]

# Test cases
test_cases = [
    [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]],
    [[1], 1, [], 0, [1]],
    [[0], 0, [1], 1, [1]],
    [[5, 6, 7, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 5, 6, 7]]
]

solution = Solution()

for i, (nums1, m, nums2, n, expected_result) in enumerate(test_cases, 1):
    solution.merge(nums1, m, nums2, n)
    print(f"Test case {i} result: {expected_result == nums1}")