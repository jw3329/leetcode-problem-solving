class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # if first passenger find his own seat -> no problem
        # if not found, this person have n-1 selection to sit
        # (n-2)*f(n-1) + 1/n
        # 1/3 + 1/3*1/2 ->
        if n == 1: return 1
        return (1 + (n-2) * self.nthPersonGetsNthSeat(n-1)) / n
