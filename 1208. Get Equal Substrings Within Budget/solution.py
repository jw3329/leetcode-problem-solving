class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # convert string to abs diff
        # sliding window
        diff = [0] * len(s)
        for i in range(len(s)):
            diff[i] = abs(ord(s[i]) - ord(t[i]))
        
        i = j = 0
        curr = 0
        max_len = 0
        while j < len(s):
            curr += diff[j]
            j += 1
            while curr > maxCost:
                curr -= diff[i]
                i += 1
            max_len = max(max_len, j - i)
        return max_len
