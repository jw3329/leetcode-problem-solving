class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 0 -1 x  x'   --> new x -> -y,   new y -> x
        # 1  0 y  y'
        # x -> -y, y -> -x --> y
        # make x y transition, then swap top bottom
        n = len(mat)
        def swap_diag():
            for i in range(n - 1):
                for j in range(n - i - 1):
                    mat[i][j], mat[n-1-j][n-1-i] = mat[n-1-j][n-1-i], mat[i][j]
        
        def swap_top_bottom():
            i = 0
            j = n - 1
            while i < j:
                for k in range(n):
                    mat[i][k], mat[j][k] = mat[j][k], mat[i][k]
                i += 1
                j -= 1
            
        def same():
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]: return False
            return True
                
        
        for _ in range(4):
            swap_diag()
            swap_top_bottom()
            if same(): return True
        return False
