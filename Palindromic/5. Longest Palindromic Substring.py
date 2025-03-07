class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        for i in range(len(s)):
            p1 = self.get_palindrome(s, i, i+1)
            p2 = self.get_palindrome(s, i, i)
            # Choose the longest string in [p, p1, p2]
            p = max([p, p1, p2], key=lambda x: len(x))
        return p
    
    def get_palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


"""
Expand Around Center Solution
Time Complexity : O(n^2)
Only 2n-1 centers for the center of a palindrome can be in between two letters
For example, abba's center is between the two 'b's

For example: s={badad}
Pass 1: l = -1, r = 1
Pass 2: l = 0,  r = 2
Pass 3: l = -1, r = 3
Pass 4: l = 1, r = 3
Pass 5: l = 0, r = 4
Pass 6: l = 2, r = 4
Pass 7: l = 3, 4 = 5
"""