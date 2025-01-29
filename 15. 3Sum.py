class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.SortingAndTwoPointer(nums)
        # return self.WithoutSorting(nums)


    # Use Sorting, O(N^2)
    def SortingAndTwoPointer(self, nums):
        nums.sort() # sorting
        added = set()
        out = []
        for i in range(len(nums) - 1, -1, -1):
            last = nums[i]
            start, end = 0, i - 1 # two pointer
            while start < end:
                s = last + nums[start] + nums[end]
                if s == 0:
                    if (last, nums[start], nums[end]) not in added: out.append([last, nums[start], nums[end]])
                    added.add((last, nums[start], nums[end]))
                    start += 1
                elif s > 0:
                    end -= 1
                else: start += 1
        return out
    # Not use Sorting, O(N^2)
    # When a<=b<=c and a+b+c = 0 
    # must be (a=0, b=0, c=0) OR (a<0, c > 0 and b = -(a+c))
    def WithoutSorting(self, nums):
        # positive and negative number
        pos = defaultdict(int)
        neg = defaultdict(int)
        for x in nums:
            if x > 0 : pos[x] +=1
            else: neg[x] += 1
                
        ans = set()
        # zero number
        if 0 in neg and neg[0] >= 3:
            ans.add((0,0,0))
        for x in neg:
            for y in pos:
                if -x-y == y and pos[y] <2 or -x-y == x and neg[x] < 2:
                    continue
                if -x-y in pos or -x-y in neg :
                    ans.add(tuple(sorted([x, y, -x-y]))) # Only sort x, y and -x-y
        return list(ans)
    
    """ 
Sorting Method
For Example: list = [-1,0,1,2,-1,-4]
Pass 1 : last = 2, start = 0, end = 4, s = -2, 2 ,1 ,0
Pass 2 : last = 1, start = 0, end = 3, s = -3, 0, 0
Pass 3 : last = 0, start = 0, end = 2, s = -5, -2
Pass 4 : last = -1, start = 0, end = 1, s = -6
Pass 5 : last = -1,  start = 0, end = 0, 
Pass 6 : last = -4, start = 0, end = -1
added = {(1, -1, 0), (2, -1, -1)}
out = [[2, -1, -1], [1, -1, 0]]

Without Sorting Method
For Example: list = [-1,0,1,2,-1,-4]
pos = {1: 1, 2: 1}, neg = {-1: 2, 0: 1, -4: 1}, ans = {}
Pass 1 : x = -1, y = 1, -x-y = 0
Pass 2 : x = -1, y = 2, -x-y = -1
Pass 3 : x = 0, y = 1, -x-y = -1
Pass 4 : 
         x = 0, y = 2 
         -> x = -4, y = 1 
         -> x = -4, y = 2, -x-y = 2, pos[y] = 1
"""