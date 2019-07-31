class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        row = len(board)
        col = len(board[0])
        for i in range(row):
            self.check(board,i,0)
            if col > 1:
                self.check(board,i,col-1)
        
        for j in range(col):
            self.check(board,0,j)
            if row > 1:
                self.check(board,row-1,j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                    
        for i in range(row):
            for j in range(col):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                    
    def check(self,board,i,j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return
        if board[i][j] == 'O':
            board[i][j] = '1'
            self.check(board,i+1,j)
            self.check(board,i,j+1)
            self.check(board,i-1,j)
            self.check(board,i,j-1)

