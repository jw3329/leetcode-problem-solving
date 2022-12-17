class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # king that makes top, bottom, left, right and find all answers
        res = []
        queens = {(i,j) for i, j in queens}
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                for k in range(1,8):
                    x = i*k + king[0]
                    y = j*k + king[1]
                    if (x,y) in queens:
                        res.append([x,y])
                        break
        return res
