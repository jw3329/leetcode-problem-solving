class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        num = nums[0]
        for i in range(1, len(nums)):
            # check absolute value
            if abs(num) > abs(nums[i]):
                num = nums[i]
            elif abs(num) == abs(nums[i]):
                if num < nums[i]:
                    num = nums[i]
        return num
