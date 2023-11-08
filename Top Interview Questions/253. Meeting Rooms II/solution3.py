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
        res = 0
        # two lists, start and end, then sort
        # track activated room then return
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        i = j = 0
        active = res = 0
        while i < len(intervals) and j < len(intervals):
            # if smallest end is more than smallest start,
            # then we need one more room activated,
            if start[i]  < end[j]:
                active += 1
                i += 1
            # if we have smallest end <= smallest start, then we deactivate
            else:
                active -= 1
                j += 1
            # track maximum room
            res = max(res, active)
        return res
