class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        # all directions are equally costed
        m = len(rowCosts)
        n = len(colCosts)
        res = 0
        while startPos[0] != homePos[0]:
            # check biggerness, if startPos is smaller, then increment by one, then add to the cost
            if startPos[0] < homePos[0]:
                res += rowCosts[startPos[0]+1]
                startPos[0] += 1
            else:
                res += rowCosts[startPos[0]-1]
                startPos[0] -= 1
        # do same for col
        while startPos[1] != homePos[1]:
            # check biggerness, if startPos is smaller, then increment by one, then add to the cost
            if startPos[1] < homePos[1]:
                res += colCosts[startPos[1]+1]
                startPos[1] += 1
            else:
                res += colCosts[startPos[1]-1]
                startPos[1] -= 1
        return res
