from typing import (
    List,
)
from lintcode import (
    Interval,
)

import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        # track minimum end time, if new things are after minimum
        # we don't need to create, but if it has conflict, then we should increment
        # sort by start time, and put end time into heap
        # if new start is more than heap end, then pop, then move forward
        intervals.sort(key=lambda x: x.start)
        res = 0
        heap = []
        for interval in intervals:
            heapq.heappush(heap, interval.end)
            # check now
            if interval.start >= heap[0]:
                heapq.heappop(heap)
            else:
                res += 1
        return res
