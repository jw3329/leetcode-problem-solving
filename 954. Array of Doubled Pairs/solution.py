class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # counter
        # for each, check if available double 
        # if available, then -1 of it
        # check if all values are 0
        counter = collections.Counter(arr)
        # sort by abs of key
        keys = sorted(counter.keys(), key=lambda x: abs(x))
        # then iterate half of keys
        # 0000
        # 1111
        for key in keys:
            if counter[key] > counter[2 * key]: return False
            counter[2 * key] -= counter[key]
        return True
