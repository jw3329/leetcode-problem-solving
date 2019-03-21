class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = collections.Counter(nums)
        limit = len(nums) // 3
        res = []
        for key,val in nums_dict.items():
            if val > limit: res.append(key)
        return res
