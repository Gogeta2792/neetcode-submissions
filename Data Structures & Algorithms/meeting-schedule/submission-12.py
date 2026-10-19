"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True 

        intervals.sort(key = lambda i:i.start)

        end = intervals[0].end

        for i in range(1, len(intervals)):
            newStart, newEnd = intervals[i].start, intervals[i].end

            if newStart < end:
                return False
            else:
                end = newEnd

        return True