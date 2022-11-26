class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # set up graph of bidirectional
        # count using set, using sorted
        # count maximum and return
        counts = [0] * n
        connected = [[False] * n for _ in range(n)]
        for road in roads:
            counts[road[0]] += 1
            counts[road[1]] += 1
            connected[road[0]][road[1]] = True
            connected[road[1]][road[0]] = True
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, counts[i] + counts[j] - connected[i][j])
        return res
