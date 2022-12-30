class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # since 0 ~ n-1
        for i in range(len(nums)):
            if abs(nums[i] - i) > 1: return False
        return True
