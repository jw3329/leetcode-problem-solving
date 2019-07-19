class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            xor = xor ^ i ^ nums[i]
        return xor ^ len(nums)
