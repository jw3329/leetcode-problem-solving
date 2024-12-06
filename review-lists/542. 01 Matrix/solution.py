class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # if found 1, find upper, left 0
        # do min + 1
        # do min of two
        # start from up
        # start from bot
        
        # do bfs first
        dirs = [0,1,0,-1,0]
        queue = deque([])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
        
        # now iterate queue
        while queue:
            i, j = queue.popleft()
            # now check
            for k in range(4):
                ii = i + dirs[k]
                jj = j + dirs[k+1]
                if ii < 0 or ii >= len(mat) or jj < 0 or jj >= len(mat[0]): continue
                # skip already proceeded
                if mat[ii][jj] != -1: continue
                # since it's trial generated from valid
                mat[ii][jj] = mat[i][j] + 1
                queue.append((ii,jj))
        return mat
            
                
