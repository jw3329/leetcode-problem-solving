class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        # check max val
        max_val = max(counter.values())
        if max_val <= len(nums) // 2:
            if len(nums) % 2 == 1: return 1
            return 0
        return 2 * max_val - len(nums)
