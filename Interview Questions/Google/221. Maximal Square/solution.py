class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        max_length = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    while True:
                        max_length_trial = max_length + 1
                        square = True
                        for k in range(i,i+max_length_trial):
                            for l in range(j,j+max_length_trial):
                                if k == m or l == n or matrix[k][l] == '0': 
                                    square = False
                                    break
                            if not square:
                                break
                        if square:
                            max_length += 1
                        else:
                            break
        return max_length ** 2
