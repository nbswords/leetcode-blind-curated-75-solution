class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [True] + [False] * len(s) # dp[0] = True, because empty string is always in wordDict
        for i in range(1, len(s) + 1):
            for word in wordDict:
                # Why is s[i-len(word):i] ?
                # because the length of matched substring must be equal to len(word)
                # So, we only need to set the search window to this length
                if s[i-len(word):i] == word:
                    if dp[i-len(word)] == True:
                        dp[i] = True
        return dp[-1]

"""
Dynamic Programming
For Example: s = "leetcode", wordDict = ["leet","code"]
Initial dp = [True, False, False, False, False, False, False, False, False], len(s) = 8

Pass 1: i=1, s[i-len(word):i] = "", word = "leet"
Pass 2: i=1, s[i-len(word):i] = "", word = "code"
Pass 3: i=2, s[i-len(word):i] = "", word = "leet"
Pass 4: i=2, s[i-len(word):i] = "", word = "code"
Pass 5: i=3, s[i-len(word):i] = "", word = "leet"
Pass 6: i=3, s[i-len(word):i] = "", word = "code"

Pass 7: i=4, s[i-len(word):i] = "leet", word = "leet", Matched, dp[4] = True
Pass 8: i=4, s[i-len(word):i] = "leet", word = "code"

Pass 9: i=5, s[i-len(word):i] = "eetc", word = "leet"
Pass 10: i=5, s[i-len(word):i] = "eetc", word = "code"

Pass 11: i=6, s[i-len(word):i] = "etco", word = "leet"
Pass 12: i=6, s[i-len(word):i] = "etco", word = "code"

Pass 13: i=7, s[i-len(word):i] = "tcod", word = "leet"
Pass 14: i=7, s[i-len(word):i] = "tcod", word = "code"

Pass 15: i=8, s[i-len(word):i] = "code", word = "leet"
Pass 16: i=8, s[i-len(word):i] = "code", word = "code", Matched, dp[8] = True

Fianl dp = [True, False, False, False, True, False, False, False, True]
"""