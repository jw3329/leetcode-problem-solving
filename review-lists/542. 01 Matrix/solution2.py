class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # if found 1, find upper, left 0
        # do min + 1
        # do min of two
        # start from up
        # start from bot
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0: continue
                top = mat[i-1][j] if i - 1 >= 0 else sys.maxsize
                left = mat[i][j-1] if j - 1 >= 0 else sys.maxsize
                # now compare
                mat[i][j] = min(top,left) + 1
        # now do bottom right to top left
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                if mat[i][j] == 0: continue
                bottom = mat[i+1][j] if i + 1 < len(mat) else sys.maxsize
                right = mat[i][j+1] if j + 1 < len(mat[0]) else sys.maxsize
                # now compare
                mat[i][j] = min(mat[i][j], min(bottom, right) + 1)
        return mat
