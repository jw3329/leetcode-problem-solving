class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_ans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_ans = max(max_ans, i - stack[-1])
        return max_ans
