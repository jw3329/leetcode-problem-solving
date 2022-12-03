class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # dp[i] -> num of subarrays ending nums[i]
        dp = [0] * len(nums)
        # if nums[i] < L -> then dp[i] = dp[i-1]
        # if nums[i] > R -> dp[i] = 0, prev = i
        # if in between, prev+1 ~ i -> i - prev
        prev = -1
        for i in range(len(nums)):
            if i > 0 and nums[i] < left:
                dp[i] = dp[i-1]
            elif nums[i] > right:
                prev = i
            elif left <= nums[i] <= right:
                dp[i] = i - prev
        return sum(dp)
