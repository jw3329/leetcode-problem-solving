class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for c in s:
            if c not in par_dict:
                stack.append(c)
            else:
                if not stack or stack.pop() != par_dict[c]: return False
        return len(stack) == 0
