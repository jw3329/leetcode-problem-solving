class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # no addition, subtraction only
        # 1 4 5 6
        # if pick i, res will be all left side + right side - curr value
        # sort first, make distinct beans
        # get all left addition values, right addition values
        # iterate, left addition + total - curr left sum, then get minimum value of it
        beans.sort()
        total = sum(beans)
        res = sys.maxsize
        for i in range(len(beans)):
            curr = total - beans[i] * (len(beans) - i)
            res = min(res, curr)
        return res
