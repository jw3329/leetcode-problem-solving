class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # max points cannot be determined by greedy
        # we grab max of f(0, each col)
        # f(i,j) -> points[i][j] + f(i+1, k) - abs(j - k) for k in col range
        m = len(points)
        n = len(points[0])
        dp = [[0] * n for _ in range(m)]
        
        for i in range(n):
            dp[0][i] = points[0][i]
        
        for i in range(1,m):
            left = [0] * n
            right = [0] * n
            left[0] = dp[i-1][0]
            for k in range(1, n):
                left[k] = max(left[k-1], dp[i-1][k] + k)
            right[n-1] = dp[i-1][n-1] - (n-1)
            for k in range(n-2,-1,-1):
                right[k] = max(right[k+1], dp[i-1][k] - k)
            
            for j in range(n):
                dp[i][j] = max(left[j] - j, right[j] + j) + points[i][j]
        
        return max(dp[m-1])
