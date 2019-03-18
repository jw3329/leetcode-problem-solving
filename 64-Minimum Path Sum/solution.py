class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1: dp[i][j] = grid[i][j]
                else:
                    adding = 0
                    if i + 1 >= m:
                        adding = dp[i][j+1]
                    elif j + 1 >= n:
                        adding = dp[i+1][j]
                    else:
                        adding = min(dp[i+1][j],dp[i][j+1])
                    dp[i][j] = grid[i][j] + adding
        return dp[0][0]
