class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        res = 0
        count = [0] * 10
        for num in nums:
            # check digit one by one
            for i in range(1, 10):
                if gcd(i, num % 10) == 1:
                    res += count[i]
            # we change left prefix first digit
            while num >= 10: num //= 10
            count[num % 10] += 1
        return res
