class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for number in range(len(nums) + 1):
            if number not in nums_set:
                return number

"""
Time Complexity: O(n)
"""