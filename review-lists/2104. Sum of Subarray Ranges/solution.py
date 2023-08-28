class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # i and j, then find max and min of it, then calculate
        # iterating i and j, find max and min individual
        # then we make those sums
        n = len(nums)
        max_vals = [[0] * n for _ in range(n)]
        min_vals = [[0] * n for _ in range(n)]
        # we calculate each
        for i in range(n):
            max_val = nums[i]
            min_val = nums[i]
            for j in range(i,n):
                max_val = max(max_val, nums[j])
                min_val = min(min_val, nums[j])
                max_vals[i][j] = max_val
                min_vals[i][j] = min_val
        # now make sum of it
        res = 0
        for i in range(n):
            for j in range(i,n):
                res += max_vals[i][j] - min_vals[i][j]
        return res
