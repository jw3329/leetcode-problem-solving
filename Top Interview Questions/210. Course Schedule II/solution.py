class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        degrees = [0 for _ in range(numCourses)]
        
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            degrees[pre[0]] += 1
        
        queue = []
        for i in range(numCourses):
            if not degrees[i]: queue.append(i)
        res = []
        while queue:
            curr = queue.pop(0)
            numCourses -= 1
            res.append(curr)
            for adj_node in adj[curr]:
                degrees[adj_node] -= 1
                if not degrees[adj_node]:
                    queue.append(adj_node)
        return res if numCourses == 0 else []
