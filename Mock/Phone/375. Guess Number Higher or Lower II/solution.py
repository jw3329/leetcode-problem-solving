class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # start = 1
        # end = n
        # res = 0
        # while start < end:
        #     mid = (start + end) // 2
        #     res += mid
        #     start = mid + 1
        # return res
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for j in range(2,n+1):
            for i in range(j-1,0,-1):
                min_val = sys.maxsize
                for k in range(i+1,j):
                    min_val = min(min_val, k + max(dp[i][k-1],dp[k+1][j]))
                dp[i][j] = i if i + 1 == j else min_val
        return dp[1][n]
