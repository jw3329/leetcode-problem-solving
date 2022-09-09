class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = [0] * 26
        visited = [False] * 26
        for c in s:
            index = ord(c) - ord('a')
            res[index] += 1
        stack = []
        for c in s:
            index = ord(c) - ord('a')
            res[index] -= 1
            if visited[index]: continue
            while stack and c < stack[-1] and res[ord(stack[-1]) - ord('a')] > 0:
                visited[ord(stack.pop()) - ord('a')] = False
            stack.append(c)
            visited[index] = True
        return ''.join(stack)
