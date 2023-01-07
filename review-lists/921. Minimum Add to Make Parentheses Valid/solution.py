class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # if open, 
        res = 0
        diff = 0
        for i in range(len(s)):
            if s[i] == '(':
                if diff < 0:
                    res += abs(diff)
                    diff = 0
                diff += 1
            else:
                diff -= 1
        return res + abs(diff)
