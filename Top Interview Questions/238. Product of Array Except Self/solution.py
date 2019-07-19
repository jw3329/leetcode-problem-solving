class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        res[0] = 1
        for i in range(1,len(res)):
            res[i] = res[i-1] * nums[i-1]
        
        right = 1
        for i in range(len(res)-1,-1,-1):
            res[i] *= right
            right *= nums[i]
        return res
