class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for word in words:
            found = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        # if it found, then put the word into res
                        if self.dfs(board,i,j,word,visited):
                            res.append(word)
                            found = True
                            break
                if found: break
        return res
    
    def dfs(self,board,i,j,word,visited):
        if not word: return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return False
        if board[i][j] != word[0]: return False
        if visited[i][j]: return False
        
        row_dir = [0,-1,0,1]
        col_dir = [1,0,-1,0]
        visited[i][j] = True
        for k in range(4):
            if self.dfs(board,i+row_dir[k],j+col_dir[k],word[1:],visited):
                visited[i][j] = False
                return True
        visited[i][j] = False
        return False
