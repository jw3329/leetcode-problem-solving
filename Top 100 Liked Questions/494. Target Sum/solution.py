class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.memo = [[-sys.maxsize] * 2001 for _ in range(len(nums))]
        return self.helper(nums,0,0,S)
    
    def helper(self,nums,i,curr,S):
        if i == len(nums):
            return curr == S
        if self.memo[i][curr + 1000] != -sys.maxsize:
            return self.memo[i][curr + 1000]
        self.memo[i][curr + 1000] = self.helper(nums,i+1,curr+nums[i],S) + self.helper(nums,i+1,curr-nums[i],S)
        return self.memo[i][curr + 1000]
