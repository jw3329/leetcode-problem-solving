class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -0x80000000 and divisor == -1: return 0x7fffffff
        ans = 0
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            temp = divisor
            m = 1
            while temp << 1 <= dividend:
                temp <<= 1
                m <<= 1
            dividend -= temp
            ans += m
        return sign * ans
