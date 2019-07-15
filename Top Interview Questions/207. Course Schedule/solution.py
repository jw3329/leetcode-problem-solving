class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        degree = [0 for _ in range(numCourses)]
        
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            degree[pre[0]] += 1
        queue = []
        
        for i in range(numCourses):
            if not degree[i]: queue.append(i)
        
        while queue:
            curr = queue.pop(0)
            numCourses -= 1
            for next in adj[curr]:
                degree[next] -= 1
                if not degree[next]:
                    queue.append(next)
        return numCourses == 0
