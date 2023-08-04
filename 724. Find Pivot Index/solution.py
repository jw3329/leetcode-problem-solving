class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # grab sum
        # move right
        # judge
        sum_val = sum(nums)
        i = 0
        curr = 0
        while i < len(nums):
            if curr == sum_val - curr - nums[i]:
                return i
            curr += nums[i]
            i += 1
        return -1
