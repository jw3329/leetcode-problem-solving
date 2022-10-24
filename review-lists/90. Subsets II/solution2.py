class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def helper(nums, i):
            if i == len(nums): return [[]]
            # find duplicates, skip it
            j = i + 1
            while j < len(nums) and nums[j] == nums[j-1]:
                j += 1
            after = helper(nums, j)
            # [], [2], [2,2]
            res = after
            for obj in after:
                for k in range(1,j-i+1):
                    res = res + [[nums[i]] * k + obj]
            return res
            
        
        return helper(nums, 0)
