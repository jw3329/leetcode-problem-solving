class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # a + b > c
        # if higher than c, then update c
        # else if higher than b, then update b
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0
        
