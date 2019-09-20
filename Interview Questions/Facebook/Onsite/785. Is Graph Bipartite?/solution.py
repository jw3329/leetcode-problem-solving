class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = [0] * len(graph)
        for i in range(len(graph)):
            # for the purpose that graph is not connected
            if colored[i] == 0 and not self.dfs(i,graph,colored,1): return False
        return True
    
    def dfs(self,i,graph,colored,color):
        if colored[i] != 0:
            return colored[i] == color 
        colored[i] = color
        for vertex in graph[i]:
            if not self.dfs(vertex,graph,colored,-color): return False
        return True
