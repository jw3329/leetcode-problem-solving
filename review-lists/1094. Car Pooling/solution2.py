class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001
        for trip in trips:
            stops[trip[1]] += trip[0]
            stops[trip[2]] -= trip[0]
        i = 0
        while capacity >= 0 and i <= 1000:
            capacity -= stops[i]
            i += 1
        return capacity >= 0
