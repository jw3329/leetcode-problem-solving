class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_val = prices[0]
        max_val = 0
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                max_val = max(max_val, prices[i] - min_val)
        return max_val
