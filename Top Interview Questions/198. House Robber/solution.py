class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [0 for _ in range(len(nums) + 1)]
        
        dp[-2] = nums[-1]
        
        for i in range(len(nums)-2,-1,-1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i+1])
        return dp[0]
