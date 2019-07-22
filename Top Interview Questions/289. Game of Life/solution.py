class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        before 0:
            after 0: 2
            after 1: 3

        bofore 1:
            after 0: 4
            after 1: 5
        '''
        direction = [-1,0,1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] >= 2: continue
                neighbors = 0
                for row in range(3):
                    for col in range(3):
                        if row == 1 and col == 1: continue
                        i_trial = i + direction[row]
                        j_trial = j + direction[col]
                        if i_trial >= 0 and i_trial < len(board) and j_trial >= 0 and j_trial < len(board[0]):
                            if board[i_trial][j_trial] in (1,4,5):
                                neighbors += 1
                
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 4
                    else:
                        board[i][j] = 5
                else:
                    if neighbors == 3:
                        board[i][j] = 3
                    else:
                        board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] %= 2
