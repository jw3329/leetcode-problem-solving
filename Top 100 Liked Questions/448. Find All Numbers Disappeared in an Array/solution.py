class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
