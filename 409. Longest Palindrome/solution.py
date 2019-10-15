class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        count = 0
        
        for c in s:
            if c not in char_set:
                char_set.add(c)
            else:
                char_set.remove(c)
                count += 1
        if len(char_set) != 0: return 2*count + 1
        return 2*count
