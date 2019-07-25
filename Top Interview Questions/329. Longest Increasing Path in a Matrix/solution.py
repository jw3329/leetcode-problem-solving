class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        memo = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.row_dir = [0,-1,0,1]
        self.col_dir = [1,0,-1,0]
        max_val = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_val = max(max_val, self.dfs(matrix,i,j,memo))
        return max_val
    
    def dfs(self,matrix,i,j,memo):
        if memo[i][j]: return memo[i][j]
        
        max_val = 1
        
        for k in range(4):
            row_trial = i + self.row_dir[k]
            col_trial = j + self.col_dir[k]
            if row_trial >= 0 and row_trial < len(matrix) and col_trial >= 0 and col_trial < len(matrix[0]) and matrix[row_trial][col_trial] > matrix[i][j]:
                max_val = max(max_val, 1 + self.dfs(matrix,row_trial,col_trial,memo))
        memo[i][j] = max_val
        return max_val
        
        
