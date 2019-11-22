class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >= n // 2: return self.quick_solve(prices)
        
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1,k+1):
            temp_max = -prices[0]
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1], temp_max + prices[j])
                temp_max = max(temp_max, dp[i-1][j-1] - prices[j])
        return dp[k][n-1]
    
    def quick_solve(self,prices):
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]: res += prices[i] - prices[i-1]
        return res
