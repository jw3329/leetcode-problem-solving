class Solution:
    def exist(self, board, word) -> bool:
        m = len(board)
        n = len(board[0])
        
        def dfs(board,i,j,word,visited,current):
            if current == word: return True
            if i < 0 or i >= m or j < 0 or j >= n: return False
            if current != word[:len(current)]: 
                return False
            if visited[i][j]: return False
            visited[i][j] = True
            row = [0,-1,0,1]
            col = [1,0,-1,0]
            for k in range(4):
                if dfs(board,i+row[k],j+col[k],word,visited,current + board[i][j]): return True
            visited[i][j] = False
            return False
        
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(board,i,j,word,visited,''): return True
        return False        




solution = Solution()

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = 'ABCB'

board2 = [["a","b"],["c","d"]]

word2 = "acdb"

print(solution.exist(board,word))
