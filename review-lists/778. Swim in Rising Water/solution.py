class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = set([(0, 0)])
        res = 0
        x_dir = [1,0,-1,0]
        y_dir = [0,1,0,-1]
        while heap:
            val, i, j = heapq.heappop(heap)
            res = max(res, val)
            if i == j == N-1: return res
            for k in range(4):
                ii = i + x_dir[k]
                jj = j + y_dir[k]
                if 0 <= ii < N and 0 <= jj < N and (ii, jj) not in seen:
                    seen.add((ii, jj))
                    heapq.heappush(heap, (grid[ii][jj], ii, jj))
