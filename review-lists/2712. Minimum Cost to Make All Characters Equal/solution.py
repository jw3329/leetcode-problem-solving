class Solution:
    def minimumCost(self, s: str) -> int:
        # if 0101010101
        # 0010 -> 0001 -> 0000
        res = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res += min(i, len(s) - i)
        return res
