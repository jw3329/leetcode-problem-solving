class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    self.dfs(grid,i,j,visited)
        return count    

    def dfs(self,grid,i,j,visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return
        if visited[i][j]: return
        if grid[i][j] == '0': return
        visited[i][j] = True
        col_dir = [1,0,-1,0]
        row_dir = [0,-1,0,1]
        for k in range(4):
            self.dfs(grid,i+row_dir[k],j+col_dir[k],visited)
