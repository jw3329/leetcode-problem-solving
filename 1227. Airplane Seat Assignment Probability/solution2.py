class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        res = 1
        for i in range(2, n+1):
            res = (1 + (i-2) * res) / i
        return res
