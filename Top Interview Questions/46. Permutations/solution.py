class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        previous_permute = self.permute(nums[:-1])
        res = []
        for permute_list in previous_permute:
            for i in range(len(permute_list)+1):
                res.append(permute_list[:i] + [nums[-1]] + permute_list[i:])
        return res
