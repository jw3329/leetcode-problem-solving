class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # all zeros from end into array
        # find from very top and swap it
        zeros = [0] * len(grid)
        for i in range(len(grid)):
            count = 0
            j = len(grid) - 1
            while j >= 0 and grid[i][j] == 0:
                count += 1
                j -= 1
            zeros[i] = count
        swaps = 0
        # swap from top
        for i in range(len(grid)):
            required = len(grid) - 1 - i
            if zeros[i] < required:
                j = i
                while j < len(grid) and zeros[j] < required:
                    j += 1
                if j == len(grid): return -1
                # add up numbers with swaps
                while j > i:
                    # swap
                    zeros[j], zeros[j-1] = zeros[j-1], zeros[j]
                    j -= 1
                    swaps += 1
        return swaps
