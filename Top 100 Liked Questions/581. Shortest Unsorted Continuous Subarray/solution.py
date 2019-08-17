class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        end = -2
        start = -1
        min_val = nums[-1]
        max_val = nums[0]
        
        for i in range(1,len(nums)):
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[len(nums) - 1 - i])
            if nums[i] < max_val:
                end = i
            if nums[len(nums) - 1 - i] > min_val:
                start = len(nums) - 1 - i
        return end - start + 1
