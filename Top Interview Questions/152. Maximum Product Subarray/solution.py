class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = min_val = max_val = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                temp = max_val
                max_val = min_val
                min_val = temp
            max_val = max(nums[i], max_val * nums[i])
            min_val = min(nums[i], min_val * nums[i])
            res = max(res, max_val)
        return res
