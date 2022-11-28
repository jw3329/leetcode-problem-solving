class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # we sort by start first
        # we've got space first, iterate trip, reduce space
        # track space info, number of destinations
        # if new trip start is less than number of destinations so far, then we pop, then make it
        # using heap
        track = []
        trips.sort(key=lambda x: x[1])
        for trip in trips:
            # we pop first
            while track and track[0] <= trip[1]:
                heapq.heappop(track)
            # if to insert with heap is more than cap, then return false
            if len(track) + trip[0] > capacity: return False
            # insert into heap
            for _ in range(trip[0]):
                heapq.heappush(track, trip[2])
        return True
