class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # count number of total 1
        # dfs from boundary, and subtract
        total = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n: return 0
            if grid[i][j] == 0: return 0
            grid[i][j] = 0
            dirs = [1,0,-1,0,1]
            res = 1
            for k in range(4):
                ii = i + dirs[k]
                jj = j + dirs[k+1]
                res += dfs(ii,jj)
            return res
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: total += 1
        for i in range(m):
            if grid[i][0] == 1:
                total -= dfs(i,0)
            if grid[i][n-1] == 1:
                total -= dfs(i,n-1)
        for j in range(n):
            if grid[0][j] == 1:
                total -= dfs(0,j)
            if grid[m-1][j] == 1:
                total -= dfs(m-1,j)
        return total
