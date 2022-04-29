class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # pick 2 nums each without index dup
        nums.sort()
        left = 0
        right = len(nums) - 1
        res = 0
        while left < right:
            val = nums[left] + nums[right]
            if val == k: 
                res += 1
                left += 1 
                right -= 1
            elif val < k:
                left += 1
            else:
                right -= 1
        return res
