class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
#         return self.helper(grid,0,0)
    
#     def helper(self,grid,i,j):
        
#         return grid[i][j] + min(self.helper(grid,i+1,j), self.helper(grid,i,j+1))

        m,n = len(grid), len(grid[0])
    
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp[i][j] ==> from grid[i][j] to bottom right, minimum path
        dp[-1][-1] = grid[-1][-1]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1: continue
                adding = 0
                if i + 1 >= m:
                    adding = dp[i][j+1]
                elif j + 1 >= n:
                    adding = dp[i+1][j]
                else:
                    adding = min(dp[i][j+1], dp[i+1][j])
                dp[i][j] = grid[i][j] + adding
        return dp[0][0]
