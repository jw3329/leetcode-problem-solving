class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # append -> only thing to add
        # find count of each letter
        # max - min then add up
        s_count = [0] * 26
        t_count = [0] * 26
        
        for c in s:
            s_count[ord(c) - ord('a')] += 1
            
        for c in t:
            t_count[ord(c) - ord('a')] += 1
            
        # compare each and add up the count
        res = 0
        for i in range(26):
            res += abs(s_count[i] - t_count[i])
        return res
