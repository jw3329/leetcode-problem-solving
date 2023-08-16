class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # union find doesn't work -> only end point we can know
        # form up graph, check if graph is reachable
        # in 2d array, memo all possibilities
        # then query, we get answer
        
        def mark_reachable(i):
            # check graphs pointing
            if i not in graph: return
            reachable[i][i] = True
            for j in graph[i]:
                # if already marked i,j then it means
                # all j marked will be reachable from i
                if reachable[i][j]: continue
                reachable[i][j] = True
                mark_reachable(j)
                # mark all available routes from j
                for k in range(numCourses):
                    reachable[i][k] |= reachable[j][k]
                
                    
        
        # form up graph
        graph = dict()
        for pre in prerequisites:
            # route
            if pre[0] not in graph:
                graph[pre[0]] = []
            graph[pre[0]].append(pre[1])
        # after forming up graph, form up 2d array to check if it's reachable
        reachable = [[False] * numCourses for _ in range(numCourses)]
        # fill up reachability
        for i in range(numCourses):
            mark_reachable(i)
        
        # after marking, we check the queries
        res = []
        for query in queries:
            res.append(reachable[query[0]][query[1]])
        return res
