class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        # sort, get maximum consecutives
        special.sort()
        res = max(special[0] - bottom, top - special[-1])
        for i in range(1, len(special)):
            res = max(res, special[i] - special[i-1] - 1)
        return res
