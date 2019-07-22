class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            max_val = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    max_val = max(max_val, dp[j] + 1)
            dp[i] = max_val
        return max(dp)
