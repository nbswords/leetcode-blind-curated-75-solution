class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #       Greedyly jump to farest position
        start, end = 0, 0
        while end < len(nums) - 1:
            start, end = end, max(i + nums[i] for i in range(start, end + 1))
            if start == end:
                return False
        return True
