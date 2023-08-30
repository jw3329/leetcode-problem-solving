class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            d = 2
            last_d = 0
            while d * d <= num:
                if num % d == 0:
                    if last_d == 0:
                        last_d = d
                    else:
                        last_d = 0
                        break
                d += 1
            if last_d != 0 and num // last_d != last_d:
                res += 1 + num + last_d + num // last_d
        return res
