class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        res = ''
        for i in range(len(s)):
            index = (i + k) % len(s)
            res += s[index]
        return res
