class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeros = 0
        seconds = 0
        for i in range(len(s)):
            zeros += s[i] == '0'
            if s[i] == '1' and zeros > 0:
                seconds = max(seconds + 1, zeros)
        return seconds
