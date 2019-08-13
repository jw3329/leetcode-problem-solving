class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m,n = len(matrix), len(matrix[0])
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        maxsqlen = 0
        
        for i in range(1,m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j]) + 1
                    maxsqlen = max(maxsqlen, dp[i][j])
        return maxsqlen ** 2
