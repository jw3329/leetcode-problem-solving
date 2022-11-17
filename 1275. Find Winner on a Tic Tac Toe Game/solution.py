class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a_row = [0] * 3
        a_col = [0] * 3
        b_row = [0] * 3
        b_col = [0] * 3
        a_d1 = a_d2 = b_d1 = b_d2 = 0
        for i in range(len(moves)):
            r = moves[i][0]
            c = moves[i][1]
            if i % 2 == 1:
                b_row[r] += 1
                if b_row[r] == 3: return 'B'
                b_col[c] += 1
                if b_col[c] == 3: return 'B'
                if r == c:
                    b_d1 += 1
                    if b_d1 == 3: return 'B'
                if r + c == 2:
                    b_d2 += 1
                    if b_d2 == 3: return 'B'
            else:
                a_row[r] += 1
                if a_row[r] == 3: return 'A'
                a_col[c] += 1
                if a_col[c] == 3: return 'A'
                if r == c:
                    a_d1 += 1
                    if a_d1 == 3: return 'A'
                if r + c == 2:
                    a_d2 += 1
                    if a_d2 == 3: return 'A'
        return 'Draw' if len(moves) == 9 else 'Pending'
