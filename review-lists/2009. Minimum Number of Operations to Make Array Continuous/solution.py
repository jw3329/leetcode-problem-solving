class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # i ~ j, j -> first element out of range of nums[i] + N
        # continuous elements -> i ~ j, end exclusive
        # operations needed -> N - (j - i)
        N = len(nums)
        nums = sorted(list(set(nums)))
        M = len(nums)
        res = N
        j = 0
        for i in range(M):
            while j < M and nums[j] < nums[i] + N: j += 1
            res = min(res, N - j + i)
        return res
