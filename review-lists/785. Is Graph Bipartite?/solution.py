class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        
        def dfs(i):
            for j in graph[i]:
                if colors[j] == colors[i]: return False
                if colors[j] == -colors[i]: continue
                colors[j] = -colors[i]
                if not dfs(j): return False
            return True
            
        
        for i in range(n):
            if colors[i] != 0: continue
            colors[i] = 1
            if not dfs(i): return False
        return True
