class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # create graph
        # remove all cycles, then append to res
        graph = collections.defaultdict(list)
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n
        
        def dfs(node, depth):
            if rank[node] >= 0: return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1: continue
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            return min_back_depth
        
        dfs(0, 0)
        return list(connections)
        
