class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        # flag: 0 --> right, 1 --> down 2 --> left 3 --> up
        # right, left --> move n-1, up, bottom --> m-1
        # once they rotate, n -= 1, m -= 1
        flag = 0
        count = 0
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 or n == 1:
            if m == 1: return matrix[0]
            else:
                return [matrix[i][0] for i in range(m)]
        i = 0
        j = 0
        total = m*n
        while count < total:
            row_move = 0
            col_move = 0
            if flag == 0 or flag == 2:
                dist = n-1
                if flag == 0:
                    col_move = 1
                else:
                    col_move = -1
            else:
                dist = m-1
                if flag == 1:
                    row_move = 1
                else:
                    row_move = -1
            if dist == 0:
                res.append(matrix[i][j])
                if flag == 0 or flag == 2:
                    i += 1
                else:
                    j += 1
                count += 1
            for k in range(dist):
                res.append(matrix[i][j])
                i += row_move
                j += col_move
                count += 1
            flag = (flag + 1) % 4
            if flag == 0:
                m -= 2
                n -= 2
                i += 1
                j += 1
        return res
