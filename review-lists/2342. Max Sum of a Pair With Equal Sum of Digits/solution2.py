class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # find two number with same digit,
        # find maximum of two number addition
        
        # iterate, and append to digit, num list
        # sort each, and find two last
        # get maximum
        
        def sum_digit(num):
            res = 0
            while num != 0:
                res += num % 10
                num //= 10
            return res
        
        d_n = [0] * 82
        res = -1
        for num in nums:
            # keep d_n maximum, track res by adding maximum with the num
            digit_sum = sum_digit(num)
            if d_n[digit_sum]:
                res = max(res, d_n[digit_sum] + num)
            d_n[digit_sum] = max(d_n[digit_sum], num)
        return res
