class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s = []
        res = [0 for _ in range(len(nums))]
        for i in range(2*len(nums)-1,-1,-1):
            while s and nums[s[-1]] <= nums[i % len(nums)]:
                s.pop()
            res[i%len(nums)] = -1 if not s else nums[s[-1]]
            s.append(i%len(nums))
        return res