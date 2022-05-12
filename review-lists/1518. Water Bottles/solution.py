class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # res += numBottles
        # restBottles += numBottles
        # numBottles -> restBottles //= exchange
        # restBottles %= exchange
        # do until we have no numBottles
        res = 0
        restBottles = 0
        while numBottles > 0:
            res += numBottles
            restBottles += numBottles
            numBottles = restBottles // numExchange
            restBottles %= numExchange
        return res
