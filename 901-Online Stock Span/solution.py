class StockSpanner:

    def __init__(self):
        self.prices = []
        self.weights = []
        

    def next(self, price: int) -> int:
        w = 1
        while self.prices and self.prices[-1] <= price:
            self.prices.pop()
            w += self.weights.pop()
        self.prices.append(price)
        self.weights.append(w)
        return w


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
