class Solution:
    def numberOfGoodSubsets(self, A):
        mod = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        dp = [1] + [0] * (1 << 10) # 0 index as 1, rest, we have from 0 to 111111111 which is total
        count = collections.Counter(A)
        for a in count:
            if a == 1: continue
            if a % 4 == 0 or a % 9 == 0 or a == 25: continue
            mask = sum(1 << i for i, p in enumerate(primes) if a % p == 0)
            for i in range(1 << 10):
                if i & mask: continue
                dp[i | mask] = (dp[i | mask] + count[a] * dp[i]) % mod
        return (1 << count[1]) * (sum(dp) - 1) % mod
