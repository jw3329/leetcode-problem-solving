class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # i and j, then find max and min of it, then calculate
        # iterating i and j, find max and min individual
        # then we make those sums
        n = len(nums)
        res = 0
        for i in range(n):
            max_val = nums[i]
            min_val = nums[i]
            for j in range(i,n):
                max_val = max(max_val, nums[j])
                min_val = min(min_val, nums[j])
                res += max_val - min_val
        return res
