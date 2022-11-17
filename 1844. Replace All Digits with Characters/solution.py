class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''
        last = ''
        for c in s:
            if 'a' <= c <= 'z':
                last = c
                res += c
            else:
                digit = int(c)
                res += chr(ord(last) + digit)
        return res
