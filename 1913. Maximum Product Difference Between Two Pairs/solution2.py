class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = 0
        bot1 = bot2 = 10001
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
            if num < bot1:
                bot2 = bot1
                bot1 = num
            elif num < bot2:
                bot2 = num
        return max1 * max2 - bot1 * bot2
