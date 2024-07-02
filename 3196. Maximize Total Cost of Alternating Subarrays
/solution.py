class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        # split by subarrays
        # for each, calculate, and grab total
        # get maximum of it
        add = nums[0]
        sub = nums[0]
        for i in range(1, len(nums)):
            temp_add = max(add, sub) + nums[i]
            temp_sub = add - nums[i]
            add = temp_add
            sub = temp_sub
        return max(add, sub)
