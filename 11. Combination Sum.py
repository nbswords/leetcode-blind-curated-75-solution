class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[[]]] + [[] for _ in range(target)]
        for num in candidates:
            for i in range(num, target + 1):
                dp[i] += [sub + [num] for sub in dp[i - num]]
        return dp[-1]

# Unbounded knapsack problem
# Example : candidates = [2,3,6,7], target = 7
# dp = [[2]]
#    = []
#    = [[2, 2]]
#    = []
#    = [[2, 2, 2]]
#    = []
#    = [[3]]
#    = [[2, 2]]
#    = [[2, 3]]
#    = [[2, 2, 2], [3, 3]]
#    = [[2, 2, 3]]
#    = [[2, 2, 2], [3, 3], [6]]
#    = [[2, 2, 3]]
#    = [[2, 2, 3], [7]]
# return dp[-1] = [[2,2,3],[7]]
