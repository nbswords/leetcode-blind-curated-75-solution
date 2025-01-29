class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #   Linear search, O(n)
        if target not in nums:
            return -1
        else:
            return nums.index(target)

#   Binary search, O(nlogn)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left+(right-left)//2
            # mid is target
            if nums[mid] == target:
                return mid
            # mid is smaller (mid is on the rotated arm)
            if nums[mid] < nums[right]:
                # search right
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                # search left
                else:
                    right = mid-1
            # mid is larger (mid is not on the rotated arm)
            else:
                # search left
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                # search right
                else:
                    left = mid+1
        return -1
# For Example : nums = [4,5,6,7,0,1,2], target = 0
# pass 1 : left = 0, right = 7-1 = 6, mid = 3, mid is larger than right(nums[3]=7 > nums[6]=2)
#          because target = 0, search right, left = mid + 1 = 1
# pass 2 : left = 4, right = 6, mid =  5, mid is smller than right (1 < 2)
#          search left, right = 5 - 1 = 4
# pass 3 : left = 4, right = 4, mid = 4, find mid == target
