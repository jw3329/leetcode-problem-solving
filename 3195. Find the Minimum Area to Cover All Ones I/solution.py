class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # f(i,j) -> max area from 0~i row, 0~j col
        # if 0, then min of i-1,j / i,j-1 / i-1,j-1
        # if 1, 
        l = u = sys.maxsize
        r = d = -sys.maxsize
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    l = min(l, j)
                    u = min(u, i)
                    r = max(r, j)
                    d = max(d, i)
        return (r - l + 1) * (d - u + 1)
