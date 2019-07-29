class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_set = set()
        double_set = set()
        for c in s:
            if c in char_set: double_set.add(c)
            char_set.add(c)
        
        for i, c in enumerate(s):
            if c not in double_set: return i
        return -1
