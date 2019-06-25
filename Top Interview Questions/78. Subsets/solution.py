class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        except_last_subsets = self.subsets(nums[:-1])
        res = except_last_subsets.copy()
        for subset in except_last_subsets:
            res.append(subset + [nums[-1]])
        return res
