class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        # dp[i][j] -> i person in a, j person in b
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i][0] = dp[i-1][0] + costs[i-1][0]
        for j in range(1,n+1):
            dp[0][j] = dp[0][j-1] + costs[j-1][1]
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i-1][j] + costs[i + j - 1][0], dp[i][j-1] + costs[i + j - 1][1])
        return dp[n][n]
