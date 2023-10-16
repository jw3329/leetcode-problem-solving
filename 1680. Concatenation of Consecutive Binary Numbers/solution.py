class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # 1 10 11 100
        # grab the number to be multipled
        # from last, add to shifted
        # keep the decimal
        
        def multiple(i):
            return int(math.log2(i)) + 1
        
        mod = 10**9 + 7
        res = 0
        for i in range(1,n+1):
            res = ((res << multiple(i)) % mod + i) % mod
        return res
