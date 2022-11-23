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
        
        digit_map = dict()
        for num in nums:
            digit_sum = sum_digit(num)
            if digit_sum not in digit_map:
                digit_map[digit_sum] = []
            digit_map[digit_sum].append(num)
        res = -1
        for digit in digit_map:
            if len(digit_map[digit]) < 2: continue
            sorted_list = sorted(digit_map[digit])
            res = max(res, sorted_list[-1] + sorted_list[-2])
        return res
