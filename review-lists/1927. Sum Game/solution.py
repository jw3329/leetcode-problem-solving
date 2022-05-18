class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        res = 0
        for i in range(n):
            res += (1 if i < n / 2 else -1) * (4.5 if num[i] == '?' else (ord(num[i]) - ord('0')))
        return res != 0
