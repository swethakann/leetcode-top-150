from typing import List
"""
Given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price_seen = float('inf')

        for curr_price in prices:
            if curr_price < min_price_seen:
                min_price_seen = curr_price
            max_profit = max(max_profit, curr_price - min_price_seen)

        return max_profit

# Test cases
testCases = [
    [[7, 1, 5, 3, 6, 4], 5],
    [[7, 6, 4, 3, 1], 0]
]

solution = Solution()

for i, (nums, expected_result) in enumerate(testCases, 1):
    print(f"Test case {i} result: {expected_result == solution.maxProfit(nums)}")