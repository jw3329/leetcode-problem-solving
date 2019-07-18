class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                num = num * 10 + int(s[i])
            if not ('0' <= s[i] <= '9') and s[i] != ' ' or i == len(s) - 1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = s[i]
                num = 0
        return sum(stack)
