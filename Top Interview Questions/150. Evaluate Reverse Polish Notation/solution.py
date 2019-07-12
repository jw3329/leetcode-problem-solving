import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+','-','*','/']:
                num2 = stack.pop()
                num1 = stack.pop()
                res = 0
                if token == '+':
                    res = num1 + num2
                elif token == '-':
                    res = num1 - num2
                elif token == '*':
                    res = num1 * num2
                elif token == '/':
                    res = num1 / num2
                    res = math.floor(res) if res >= 0 else math.ceil(res)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()
