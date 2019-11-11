class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        if board[click[0]][click[1]] != 'E': return board 
        mines = self.number_of_adjacent_to_mine(board, *click)
        if mines:
            board[click[0]][click[1]] = str(mines)
            return board
        board[click[0]][click[1]] = 'B'    
        directions = [1,0,-1]
        for i in range(3):
            for j in range(3):
                if directions[i] == 0 and directions[j] == 0: continue
                x = click[0] + directions[i]
                y = click[1] + directions[j]
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]): continue
                self.updateBoard(board,[x,y])
        return board
        
    def number_of_adjacent_to_mine(self,board,x,y):
        x_dir = [0,1,1,1,0,-1,-1,-1]
        y_dir = [1,1,0,-1,-1,-1,0,1]
        count = 0
        for k in range(8):
            x_try = x + x_dir[k]
            y_try = y + y_dir[k]
            if 0 <= x_try and x_try < len(board) and 0 <= y_try and y_try < len(board[0]) and board[x_try][y_try] == 'M': count += 1
        return count
