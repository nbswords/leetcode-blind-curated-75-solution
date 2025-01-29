import operator
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Maximum subarray problem with Kadane's algorithm
        max_ending_here, max_so_far = 0, 0
        # profit = price[1:] - prices
        for profit in map(operator.sub, prices[1:], prices):
            max_ending_here = max(max_ending_here + profit, 0)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

