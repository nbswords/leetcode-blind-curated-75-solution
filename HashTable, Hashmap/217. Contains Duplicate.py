class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use set, Time: O(n), Space: O(n)
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
        # Sorting, Time: O(nlogn), Space: O(1)
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False