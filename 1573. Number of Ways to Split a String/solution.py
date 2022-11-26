class Solution:
    def numWays(self, s: str) -> int:
        # count number of 1, then decide how many num to split
        # locate number of 1s, then we should determine block
        # 10101 -> A0A0A -> 2 * 2
        # if all 0, then choose n-1 space of 2 n-1C2 -> (n-1) * (n-2) / 2
        
        def split_location(location):
            res = []
            temp = []
            num = n // 3
            for i in location:
                temp.append(i)
                if len(temp) == num:
                    res.append(temp)
                    temp = []
            return res
        
        location = []
        for i in range(len(s)):
            if s[i] == '1': location.append(i)
        n = len(location)
        mod = 10**9 + 7
        if n % 3 != 0: return 0
        if n == 0: return ((len(s)-1) * (len(s)-2) // 2) % mod
        # split location into 3 basis
        splitted = split_location(location) # [[A] [B] [C]]
        return (splitted[1][0] - splitted[0][-1]) * (splitted[2][0] - splitted[1][-1]) % mod
