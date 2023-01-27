class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2*n - 1)
        visited = [False] * (n+1)
        
        def dfs(index):
            if index == len(res): return True
            if res[index] != 0: return dfs(index+1)
            for i in range(n,0,-1):
                if visited[i]: continue
                visited[i] = True
                res[index] = i
                if i == 1:
                    if dfs(index+1): return True
                elif i + index < len(res) and res[i+index] == 0:
                    res[i+index] = i
                    if dfs(index+1): return True
                    res[i+index] = 0
                res[index] = 0
                visited[i] = False
            return False
        
        dfs(0)
        return res
