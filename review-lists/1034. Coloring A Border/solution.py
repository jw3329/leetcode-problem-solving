class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        # start from row, col,
        # if grid is same as color, and if it's in the boundary, then color it
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        def dfs(i, j, from_color, to):
            if grid[i][j] != from_color or visited[i][j]: return
            visited[i][j] = True
            # do nothing if not color
            x_dir = [1,0,-1,0]
            y_dir = [0,1,0,-1]
            for k in range(4):
                ii = i + x_dir[k]
                jj = j + y_dir[k]
                # color only when curr is at boundary, or
                if ii < 0 or ii > len(grid) - 1 or jj < 0 or jj > len(grid[0]) - 1 or (not visited[ii][jj] and grid[ii][jj] != from_color):
                    grid[i][j] = to
                    continue
                dfs(ii, jj, from_color, to)
        
        dfs(row, col, grid[row][col], color)
        return grid
