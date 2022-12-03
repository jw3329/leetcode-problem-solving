class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        dp = 0
        prev = -1
        for i in range(len(nums)):
            if i > 0 and nums[i] < left:
                res += dp
            elif nums[i] > right:
                dp = 0
                prev = i
            elif left <= nums[i] <= right:
                dp = i - prev
                res += dp
        return res
