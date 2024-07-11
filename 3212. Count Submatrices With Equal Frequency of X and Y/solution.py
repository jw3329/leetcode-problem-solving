class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        # check the count of prev
        # if x, then + 1, if y, then -1
        # check the flag if containing x
        # mark all grid of this info
        # we make, dp[i][j] -> we should meet condition above
        # status + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        # initially we setup all right side, down side
        # making total, and right side is number of x
        
        class Pair:
            def __init__(self, total, x):
                self.total = total
                self.x = x
                
            def __repr__(self):
                return str([self.total, self.x])
        
        
        dp = [[Pair(0,0) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        if grid[0][0] == 'X':
            dp[0][0].total += 1
            dp[0][0].x += 1
        elif grid[0][0] == 'Y':
            dp[0][0].total -= 1
        for i in range(1, len(grid)):
            dp[i][0].total = dp[i-1][0].total
            dp[i][0].x = dp[i-1][0].x
            if grid[i][0] == 'X':
                dp[i][0].total += 1
                dp[i][0].x += 1
            elif grid[i][0] == 'Y':
                dp[i][0].total -= 1
        for j in range(1, len(grid[0])):
            dp[0][j].total = dp[0][j-1].total
            dp[0][j].x = dp[0][j-1].x
            if grid[0][j] == 'X':
                dp[0][j].total += 1
                dp[0][j].x += 1
            elif grid[0][j] == 'Y':
                dp[0][j].total -= 1
        # do now 
        for i in range(1,len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j].total = dp[i-1][j].total + dp[i][j-1].total - dp[i-1][j-1].total
                dp[i][j].x = dp[i-1][j].x + dp[i][j-1].x - dp[i-1][j-1].x
                if grid[i][j] == 'X':
                    dp[i][j].total += 1
                    dp[i][j].x += 1
                if grid[i][j] == 'Y':
                    dp[i][j].total -= 1
        # now find total of 0 for first, and > 0 for second
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dp[i][j].total == 0 and dp[i][j].x > 0: res += 1
        return res
