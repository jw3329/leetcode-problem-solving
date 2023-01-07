class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # sort then max each first and last
        nums.sort()
        max_val = 0
        for i in range(len(nums) // 2):
            max_val = max(max_val, nums[i] + nums[len(nums) - i - 1])
        return max_val
