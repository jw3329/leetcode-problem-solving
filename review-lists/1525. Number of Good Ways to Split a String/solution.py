class Solution:
    def numSplits(self, s: str) -> int:
        # left count, right -> total count - left count
        counter = collections.Counter(s)
        t_key = len(counter)
        left_set = set()
        # split right before index i
        res = 0
        for i in range(len(s)):
            left_set.add(s[i])
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                t_key -= 1
            if len(left_set) == t_key: 
                res += 1
        return res
