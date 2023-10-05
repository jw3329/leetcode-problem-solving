class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        # minimum addition will be from first digit
        # increment digit, by making 0,
        # check if it's <= target
        
        def digit_calc(num):
            curr = 0
            while num != 0:
                curr += num % 10
                num //= 10
            return curr
        
        
        curr = digit_calc(n)
        res = 0
        digit = 0
        while curr > target:
            # increment digit
            d = n % 10
            if d > 0:
                # add in res
                res += (10 - d) * (10 ** digit)
                # decrease curr
                n += (10 - d)
                curr = digit_calc(n)
            digit += 1
            n //= 10
        return res
