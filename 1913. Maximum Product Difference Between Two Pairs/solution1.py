class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        top1 = max(nums)
        top1_i = nums.index(top1)
        nums.pop(top1_i)
        top2 = max(nums)
        top2_i = nums.index(top2)
        nums.pop(top2_i)
        bottom1 = min(nums)
        bottom2_i = nums.index(bottom1)
        nums.pop(bottom2_i)
        bottom2 = min(nums)
        bottom2_i = nums.index(bottom2)
        nums.pop(bottom2_i)
        return top1 * top2 - bottom1 * bottom2
