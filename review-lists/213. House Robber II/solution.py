class Solution:
    def rob(self, nums: List[int]) -> int:
        # curr -> max of prev, curr + prev prev
        def helper(i,j):
            prev = 0
            curr = 0
            for k in range(i, j+1):
                temp = curr
                curr = max(curr, nums[k] + prev)
                prev = temp
            return curr
        
        
        if len(nums) == 1: return nums[0]
        return max(helper(0, len(nums) - 2), helper(1, len(nums) - 1))
