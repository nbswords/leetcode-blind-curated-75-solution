class Solution:
    def countSubstrings(self, s: str) -> int:
        # Sol_1: Expand Around Center
        # O(n^2) time
        ans = 0
        n = len(s)
        i, j = 0, 0
        while j < n:
            left, right = i, j
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
            if i == j:
                j += 1
            else:
                i += 1
        return ans
        # Sol_2: Manacher Algorithm
        # O(n) time
        S = '#'.join('^' + s + '$') # If s = "abc", then S = "^#a#b#c#$"
        P = [0] * len(S) # P[i] stores the radius of the longest palindrome centered at i in S.
        center, right = 0, 0
        for i in range(1, len(S) - 1): # Skip "^" and "$"
            if i < right: 
                # P[i] is set based on symmetry with respect to center
                P[i] = min(right - i, P[2 * center - i])
            while S[i + P[i] + 1] == S[i - P[i] - 1]: 
                # Expand the palindrome while the characters on both sides match.
                P[i] += 1
            if i + P[i] > right:
                # If the new palindrome extends beyond right, update center and right.
                center, right = i, i + P[i]
        # Each palindrome in S corresponds to (P[i] + 1) // 2 palindromic substrings in s.
        # Summing over all P[i] gives the total count.
        return sum((p + 1) // 2 for p in P)

"""
Expand Around Center Solution
Time Complexity : O(n^2)
Space Complexity : O(1)

Manacher Algorithm
Time Complexity : O(n)
Space Complexity : O(n)
    For example: s="abba"
    S = "^ # a # b # b # a # $"
    P = [0, 0, 1, 0, 3, 0, 3, 0, 1, 0, 0]
    (P[i] + 1) //2 = [0, 0, 1, 0, 2, 0, 2, 0, 1, 0, 0]
    Total = 6 (a, b, b, a, bb, abba)
    
"""
