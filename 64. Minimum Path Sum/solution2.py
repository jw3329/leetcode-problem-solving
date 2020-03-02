class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        memo = [[0] * n for _ in range(m)]
        
        def helper(i,j):
            if i < 0 or i >= m or j < 0 or j >= n: return sys.maxsize
            if i == m-1 and j == n-1: return grid[i][j]
            if memo[i][j] != 0: return memo[i][j]
            memo[i][j] = grid[i][j] + min(helper(i+1,j), helper(i,j+1))
            return memo[i][j]
        
        return helper(0,0)
