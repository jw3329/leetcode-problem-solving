class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.product_price = dict()
        for i in range(len(products)):
            self.product_price[products[i]] = prices[i]
        self.order = 0
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.order += 1
        # calculate the price
        total = 0
        for i in range(len(product)):
            total += amount[i] * self.product_price[product[i]]
        # if nth order, then apply discount
        if self.order % self.n == 0:
            total = total * ((100 - self.discount) / 100)
        return total
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
