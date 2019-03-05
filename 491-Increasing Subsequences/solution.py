class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        s = set()
        self.findSubsequencesHelper(nums,s)
        return list(s)
        
    def findSubsequencesHelper(self,nums,s):
        if len(nums) <= 1: return
        self.findSubsequencesHelper(nums[:-1],s)
        setList = list(s)
        for seq in setList:
            if nums[-1] >= seq[-1]:
                s.add(tuple(list(seq) + [nums[-1]]))
        for num in nums[:-1]:
            if nums[-1] >= num:
                s.add(tuple([num] + [nums[-1]]))
