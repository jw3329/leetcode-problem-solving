class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_nonzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[last_nonzero] = nums[last_nonzero],nums[i]
                last_nonzero += 1
        
