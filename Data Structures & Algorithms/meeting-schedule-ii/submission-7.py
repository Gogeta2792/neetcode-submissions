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
            start, end = interval.start, interval.end

            if not res or start < res[0]:
                heapq.heappush(res, end)
            
            else:
                heapq.heappop(res)
                heapq.heappush(res, end)
        
        return len(res)
            