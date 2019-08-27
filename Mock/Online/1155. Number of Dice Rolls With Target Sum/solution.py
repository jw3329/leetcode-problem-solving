class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        
        for i in range(1,min(f,target)+1):
            dp[1][i] = 1
        
        for i in range(2,d+1):
            for j in range(i,target+1):
                for k in range(1,min(f,j)+1):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % (10**9 + 7)
        return dp[d][target]
