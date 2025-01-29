class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Counting character as key in hashmap
        groups = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return groups.values()
