class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            # i & (i-1) is previous number, so dp[i] = dp[i & (i-1)] + 1 is to skip the last
            dp[i] = dp[i & (i-1)] + 1 
        return dp
    

"""
Bottom-up DP, Time complexity: O(n)
For example, num=5

i (decimal) | i (binary)   | i & (i - 1)   |	dp[i & (i - 1)] | dp[i]
0	        | 000	       | N/A	       |       0	        | 0 
1	        | 001	       | 000	       |     dp[0] = 0	    | 1
2	        | 010	       | 000	       |     dp[0] = 0	    | 1
3	        | 011	       | 010	       |     dp[2] = 1	    | 2
4	        | 100	       | 000	       |     dp[0] = 0	    | 1
5	        | 101	       | 100	       |     dp[4] = 1	    | 2

Output: [0,1,1,2,1,2]
"""