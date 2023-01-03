class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = [0] * len(s)
        stack = list(s)
        i = j = 0
        while j < len(s):
            stack[i] = stack[j]
            if i > 0 and stack[i-1] == stack[i]:
                count[i] = count[i-1] + 1
            else:
                count[i] = 1
            if count[i] == k: i -= k
            i += 1
            j += 1
        return ''.join(stack)[:i]
