class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        for p in [1, -1]:
            for q in [1, -1]:
                smallest = p * arr1[0] + q * arr2[0] + 0
                for i in range(len(arr1)):
                    curr = p * arr1[i] + q * arr2[i] + i
                    res = max(res, curr - smallest)
                    smallest = min(smallest, curr)
        return res
