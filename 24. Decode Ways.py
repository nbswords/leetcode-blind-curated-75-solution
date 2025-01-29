class Solution:
    def numDecodings(self, s: str) -> int:
        # Bottom-Up DP
        if s[0] == '0':
            return 0
        prev, curr = 1, 1
        for i in range(1, len(s)):
            count = 0
            if s[i] != '0':
                count += curr
            if s[i-1] == '1' or (s[i-1] == '2' and ord(s[i]) < ord('7')):
                count += prev
            prev, curr = curr, count
        return curr
