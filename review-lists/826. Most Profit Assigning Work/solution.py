class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # maximum profit should be returned
        # profit with difficulty sort desc, and sort works desc order
        # iterate profit, if things can be done with curr worker, then stay with work then move on
        # if can not be done, move profit, compare worker, return maximum profit
        zipped = list(zip(profit, difficulty))
        zipped.sort(key=lambda x: (-x[0], x[1]))
        worker.sort(reverse=True)
        # now all reversed
        res = 0
        i = 0
        j = 0
        while i < len(zipped) and j < len(worker):
            w = worker[j]
            if zipped[i][1] <= w:
                res += zipped[i][0]
                j += 1
            else:
                i += 1
        return res

