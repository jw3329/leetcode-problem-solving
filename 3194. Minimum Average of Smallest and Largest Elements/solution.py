class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left = 0
        right = len(nums) - 1
        min_val = sys.maxsize
        while left < right:
            min_val = min(min_val, (nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return min_val
