# class Solution:
#     def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
#         if board[click[0]][click[1]] == 'M':
#             board[click[0]][click[1]] = 'X'
#             return board
#         if board[click[0]][click[1]] != 'E': return board
#         mines = self.number_of_adjacent_to_mine(board, *click)
#         if mines:
#             board[click[0]][click[1]] = str(mines)
#             return board
#         board[click[0]][click[1]] = 'B'
#         directions = [1,0,-1]
#         for i in range(3):
#             for j in range(3):
#                 if directions[i] == 0 and directions[j] == 0: continue
#                 x = click[0] + directions[i]
#                 y = click[1] + directions[j]
#                 if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]): continue
#                 self.updateBoard(board,[x,y])
#         return board

#     def number_of_adjacent_to_mine(self,board,x,y):
#         x_dir = [0,1,1,1,0,-1,-1,-1]
#         y_dir = [1,1,0,-1,-1,-1,0,1]
#         count = 0
#         for k in range(8):
#             x_try = x + x_dir[k]
#             y_try = y + y_dir[k]
#             if 0 <= x_try and x_try < len(board) and 0 <= y_try and y_try < len(board[0]) and board[x_try][y_try] == 'M': count += 1
#         return count


def check_nearby(board, click):
    # check count of mine near by
    x_dir = [-1, 0, 1]
    y_dir = [-1, 0, 1]
    res = 0
    for i in range(3):
        for j in range(3):
            xx = click[0] + x_dir[i]
            yy = click[1] + y_dir[j]
            # check within boundary
            if xx < 0 or xx >= len(board) or yy < 0 or yy >= len(board[0]):
                continue
            # it's in boundary now
            if board[xx][yy] == "M":
                res += 1
    return res


def solution(board, click):
    # check first condition
    if (
        click[0] < 0
        or click[0] >= len(board)
        or click[1] < 0
        or click[1] >= len(board[0])
    ):
        return
    # if clicking empty, then check if adjacent with mine, if no mine, then more recursive
    # if clicking empty, with mine adjacent, calculate how many mines available, then return the number
    # if clicking mine, game over, then change to x
    # else, no action
    check = board[click[0]][click[1]]
    if check == "M":
        board[click[0]][click[1]] = "X"
        return
    if check == "E":
        # check nearby
        # if no nearby, then we do same check for other directions also
        # if near by, then change the number
        count = check_nearby(board, click)
        if count:
            board[click[0]][click[1]] = str(count)
        else:
            board[click[0]][click[1]] = "B"
            x_dir = [1, 0, -1, 0]
            y_dir = [0, 1, 0, -1]
            for k in range(4):
                xx = click[0] + x_dir[k]
                yy = click[1] + y_dir[k]
                solution(board, [xx, yy])


board1 = [
    ["E", "E", "E", "E", "E"],
    ["E", "E", "M", "E", "E"],
    ["E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E"],
]

solution(board1, [3, 0])
print(board1)
[
    ["B", "1", "E", "1", "B"],
    ["B", "1", "M", "1", "B"],
    ["B", "1", "1", "1", "B"],
    ["B", "B", "B", "B", "B"],
]


board2 = [
    ["B", "1", "E", "1", "B"],
    ["B", "1", "M", "1", "B"],
    ["B", "1", "1", "1", "B"],
    ["B", "B", "B", "B", "B"],
]

solution(board2, [1, 2])
print(board2)
[
    ["B", "1", "E", "1", "B"],
    ["B", "1", "X", "1", "B"],
    ["B", "1", "1", "1", "B"],
    ["B", "B", "B", "B", "B"],
]
