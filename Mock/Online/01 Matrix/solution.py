class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        while True:
            no_change = True
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != 0:
                        min_val = sys.maxsize
                        for k in range(4):
                            x = i + direction[k][0]
                            y = j + direction[k][1]
                            if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
                                min_val = min(min_val,matrix[x][y])
                        if matrix[i][j] != min_val + 1:
                            no_change = False
                            matrix[i][j] = min_val + 1
            if no_change: break
        return matrix

