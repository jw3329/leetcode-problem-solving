class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # get min value of prefix sum
        # return
        min_val = nums[0]
        sum_val = nums[0]
        for i in range(1, len(nums)):
            sum_val += nums[i]
            min_val = min(min_val, sum_val)
        return max(1 - min_val, 1)
