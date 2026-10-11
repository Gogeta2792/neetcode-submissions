"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i:i.start)
        res = []

        for interval in intervals:
            if not res or res[0] > interval.start:
                heapq.heappush(res, interval.end)
            else:
                heapq.heappop(res)
                heapq.heappush(res, interval.end)
        
        return len(res)