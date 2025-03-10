class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Sol_1: HashTable
        if len(s) != len(t):
            return False

        dict = {}
        for c in s:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1

        for c in t:
            if c not in dict:
                return False
            else:
                dict[c] -= 1
                if dict[c] < 0:
                    return False
        return True
        # Sol_2: Counter        
        # def isAnagram(self, s: str, t: str) -> bool:
        #     return collections.Counter(s) == collections.Counter(t)