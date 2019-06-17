class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        factorial_dp = [0 for _ in range(m+n-1)]
        factorial_dp[0] = 1
        for i in range(1,m+n-1):
            factorial_dp[i] = i*factorial_dp[i-1]
        return factorial_dp[m + n - 2] // (factorial_dp[n-1] * factorial_dp[m-1])
