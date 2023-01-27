class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # should sort by distance order by zipped
        # calculate how many seconds needed to be reached
        # sort seconds
        # if two duplicate element found, return
        # 2 2 3
        # 1 3 4
        # 0 0 2
        seconds = [0] * len(dist)
        for i in range(len(dist)):
            seconds[i] = math.ceil(dist[i] / speed[i])
        seconds.sort()
        res = 0
        for i in range(len(dist)):
            if i >= seconds[i]: break
            res += 1
        return res
