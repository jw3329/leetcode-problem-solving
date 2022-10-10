class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # only 2345 4567 6789
        graph = dict()
        # iterate seats to track
        for seat in reservedSeats:
            graph[seat[0]] = graph.get(seat[0], 0) | (1 << seat[1])
        # now iterate graph key, and grab maximum possible seats
        val = 0
        for seat in graph:
            count = 0
            if graph[seat] & 0b111100 == 0:
                count += 1
            if graph[seat] & 0b1111000000 == 0:
                count += 1
            if count == 0 and graph[seat] & 0b11110000 == 0:
                count = 1
            val += count
        return val + 2 * (n - len(graph))
