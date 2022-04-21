class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[set() for _ in range(n)] for _ in range(2)]
        # 0 -> red, 1 -> blue
        for i, j in redEdges:
            graph[0][i].add(j)
        for i, j in blueEdges:
            graph[1][i].add(j)
        res = [[0] * n for _ in range(2)]
        # initialize res
        # max value is 2 * n - 3 --> initializing to 2 * n
        for i in range(1, n):
            res[0][i] = 2 * n
            res[1][i] = 2 * n
        queue = deque([(0, 0), (0, 1)])
        while queue:
            vert, color = queue.popleft()
            for adj in graph[1-color][vert]:
                # if res is not been set, set it up, since it is bfs, minimum path should be priority
                if res[1-color][adj] == 2 * n:
                    res[1-color][adj] = 1 + res[color][vert]
                    queue.append((adj, 1-color))
        # find final answer, if 2 * n, then make it into -1
        ans = [0] * n
        for i in range(n):
            min_val = min(res[0][i], res[1][i])
            if min_val == 2 * n:
                min_val = -1
            ans[i] = min_val
        return ans
