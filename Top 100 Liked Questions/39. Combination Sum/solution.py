class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not target: return [[]]
        res = []
        for num in candidates:
            if target >= num:
                comb = self.combinationSum(candidates, target - num)
                for sub_comb in comb:
                    res.append([num] + sub_comb)
        new_set = set()
        new_list = []
        for sub_res in res:
            sorted_string = str(sorted(sub_res))
            if sorted_string not in new_set:
                new_list.append(sub_res)
                new_set.add(sorted_string)
        return new_list
