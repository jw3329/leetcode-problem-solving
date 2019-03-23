class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_val = prices[0]
        prev = prices[0]
        res = 0
        for i in range(1,len(prices)):
            if prices[i] < prev:
                min_val = min(min_val,prices[i])
            else:
                res = max(res,prices[i] - min_val)
            prev = prices[i]
        return res
