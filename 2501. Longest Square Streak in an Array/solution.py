class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # for each array
        # check if square is in array
        # if not, then assume it's the first one
        # do until it's not there
        # iterate, and return max
        res = 0
        num_set = set(nums)
        for num in num_set:
            if num ** (1/2) in num_set: continue
            streak = 1
            while num ** 2 in num_set:
                streak += 1
                num *= num
            res = max(res, streak)
        return res if res > 1 else -1


