class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        prev_sell = 0
        buy = -sys.maxsize
        
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell
