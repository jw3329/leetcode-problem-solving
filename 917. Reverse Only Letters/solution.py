class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left = 0
        right = len(S) - 1
        S = list(S)
        while left < right:
            while left < right and not 'a' <= S[left].lower() <= 'z':
                left += 1
            while left < right and not 'a' <= S[right].lower() <= 'z':
                right -= 1
            if left < right:
                S[left],S[right] = S[right],S[left]
                left += 1
                right -= 1
        return ''.join(S)
