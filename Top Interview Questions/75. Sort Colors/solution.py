class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        right = len(nums)
        index = 0
        # since it is only 0,1,2, make 0 to the very left side, 2 to the very right side
        # will solve the problem
        while index < right:
            if nums[index] == 0:
                left += 1
                temp = nums[left]
                nums[left] = 0
                nums[index] = temp
                if left == index: index += 1
            elif nums[index] == 2:
                right -= 1
                temp = nums[right]
                nums[right] = 2
                nums[index] = temp
            else:
                index += 1
