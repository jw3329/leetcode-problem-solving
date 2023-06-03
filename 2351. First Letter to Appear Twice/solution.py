class Solution:
    def repeatedCharacter(self, s: str) -> str:
        c_set = set()
        for c in s:
            if c in c_set:
                return c
            c_set.add(c)
        return ''
