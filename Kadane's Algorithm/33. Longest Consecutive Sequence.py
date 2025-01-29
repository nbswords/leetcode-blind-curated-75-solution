class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_ending_here, max_so_far = int(bool(nums)), 0
        for num, next_num in zip(nums, nums[1:]):
            if num == next_num: continue
            max_ending_here *= num + 1 == next_num
            max_ending_here += 1
            max_so_far = max(max_so_far, max_ending_here)
        return max(max_so_far, max_ending_here)