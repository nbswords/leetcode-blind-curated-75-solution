class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sol_1: iterative check whether result equal to target
        # O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # Sol_2: Build a Hash table with dict and enumerate()
        # O(n)
            # dict is a HashTable which Key=num_1 and Value=num_2
            dict = {}
            # i = 0,1,2,3...
            # num = number in nums with respect to i
            for i, num in enumerate(nums):
                if num in dict:
                    # num_1, num_2
                    return([dict[num], i])
                else:
                    # target = num_1 + num_2 => target - num_2 = num_1
                    dict[target - num] = i


"""
Sol_2 might be harder than Sol_1 to understand
For example: nums = [2,7,11,15], target = 9
Pass 1: num=2, i=0 then create dict[9-2] = 0
Pass 2: num=7, i=1 then found 7=9-2, so return dict[7], which is 0 and i, which is 1
"""
