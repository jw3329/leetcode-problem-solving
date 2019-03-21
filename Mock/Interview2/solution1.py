class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correspond = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in correspond:
                if stack and stack[-1] == correspond[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                    
