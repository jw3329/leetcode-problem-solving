class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # first minimum value
        # do stack, compare top with current, if curr is less than top,
        # then pop, then put subtraction
        res = prices.copy()
        stack = []
        for i, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                p, j = stack.pop()
                res[j] = p - price
            stack.append((price, i))
        return res
