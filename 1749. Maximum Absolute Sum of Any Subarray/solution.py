class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # track max prefix sum, min prefix sum, then max - min
        s = 0
        max_sum = 0
        min_sum = 0
        for num in nums:
            s += num
            max_sum = max(max_sum, s)
            min_sum = min(min_sum, s)
        return max_sum - min_sum
