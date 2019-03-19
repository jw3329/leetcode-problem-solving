class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colored = [0 for _ in range(n)]
        for i in range(n):
            if colored[i] == 0 and not self.dfsColor(i,graph,colored,1): return False
        return True
    
    def dfsColor(self,i,graph,colored,color):
        if colored[i] != 0:
            return colored[i] == color
        colored[i] = color
        for vertex in graph[i]:
            if not self.dfsColor(vertex,graph,colored,-color): return False
        return True
