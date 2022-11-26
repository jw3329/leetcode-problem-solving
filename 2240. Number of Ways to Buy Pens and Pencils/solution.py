class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # total >= A * cost1 + B * cost2
        # where A and B are integer
        # start from 0, increment by 1 -> A, then divide, then add
        res = 0
        i = 0
        max_val = max(cost1, cost2)
        min_val = min(cost1, cost2)
        while i * max_val <= total:
            rem = total - i * max_val
            res += (rem // min_val) + 1
            i += 1
        return res
