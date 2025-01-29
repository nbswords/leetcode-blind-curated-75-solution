class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Init dp = 0 as list = [m*n] using list comprehension
        dp = [[0 for i in range(n)] for j in range(m)]
        # Boundary case 1 : target is in row 0
        for i in range(m):
            dp[i][0] = 1
        # Boundary case 2 : target is in col 0
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
