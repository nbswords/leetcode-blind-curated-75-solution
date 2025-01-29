class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 使用 iterable 建立Counter
        need, missing = collections.Counter(t), len(t)
        i, I, J = 0, 0, 0
        # sliding window method using two pointer
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if (not J or s[i] == c) and not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i < J - I:
                    I, J = i, j
        return s[I:J]
