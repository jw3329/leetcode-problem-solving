class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        rearranged_string = ''
        for c in s:
            if ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'):
                rearranged_string += c
        start, end = 0, len(rearranged_string) - 1
        while start < end:
            if rearranged_string[start] != rearranged_string[end]:
                return False
            start += 1
            end -= 1
        return True
