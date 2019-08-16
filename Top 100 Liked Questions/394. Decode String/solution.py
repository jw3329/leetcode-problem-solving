class Solution:
    def decodeString(self, s: str) -> str:
        if not s: return ''
        k = ''
        stack = []
        res = ''
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(i)
            elif s[i] == ']':
                index = stack.pop()
                if not stack:
                    print(k)
                    return res + (int(k) * self.decodeString(s[index+1:i])) + self.decodeString(s[i+1:])
            if not stack:
                if '0' <= s[i] <= '9':
                    k += s[i]
                else:
                    res += s[i]
        return res
