class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        left = 0
        right = 0
        i = 0
        while i < len(s) // 2:
            if s[i] in vowels:
                left += 1
            if s[len(s) // 2 + i] in vowels:
                right += 1
            i += 1
        return left == right
