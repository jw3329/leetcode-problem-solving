class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = nums[0]
        prev = nums[0]
        for i in range(1,len(nums)):
            prev = nums[i] + (prev if prev > 0 else 0)
            max_val = max(max_val, prev)
        return max_val
