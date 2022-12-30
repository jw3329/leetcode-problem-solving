class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # max number of local inversion -> n-1
        cmax = 0
        for i in range(len(nums)-2):
            cmax = max(cmax, nums[i])
            if cmax > nums[i+2]: return False
        return True
