class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # used is a HashTable
        used = {}
        max_length = start = 0
        # i = 0,1,2...
        # char = characters in s
        for i, char in enumerate(s):
            if char in used and start <= used[char]:

                start = used[char] + 1
            else:
                # lenght ++
                max_length = max(max_length, i - start + 1)
            # Mapping char as Key and i as Value
            used[char] = i
        return max_length


"""
For example: s={abcabcbb}
Pass 1: i=0, char=a, max_length = max(0, 0-0+1), used[a] = 0
Pass 2: i=1, char=b, max_length = max(1, 1-0+1), used[b] = 1
Pass 3: i=2, char=c, max_length = max(2, 2-0+1), used[c] = 2
Pass 4: i=3, char=a, start = used[a] + 1
Pass 5: i=4, char=b, start = used[b] + 1
Pass 6: i=5, char=c, start = used[c] + 1
Pass 7: i=6, char=b, start = used[b] + 1
Pass 8: i=7, char=b, start = used[b] + 1
return max_lenght=3
"""
