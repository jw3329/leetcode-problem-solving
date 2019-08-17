class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        for i in range(len(s)):
            self.extend_palindrome(s,i,i)
            self.extend_palindrome(s,i,i+1)
        return self.count
    
    def extend_palindrome(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.count += 1
            left -= 1
            right += 1
