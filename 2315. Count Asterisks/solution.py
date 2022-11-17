class Solution:
    def countAsterisks(self, s: str) -> int:
        mode = True
        res = 0
        for c in s:
            if c == '|':
                mode = not mode
            if mode and c == '*':
                res += 1
        return res
