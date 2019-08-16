class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_val = sum(nums)
        if sum_val & 1 == 1: return False
        
        sum_val //= 2
        
        dp = [False for _ in range(sum_val + 1)]
        
        dp[0] = True
        
        for num in nums:
            for i in range(sum_val,-1,-1):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]
        return dp[sum_val]
