"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        new_intervals = sorted(intervals, key = lambda i : i.start)

        prev = 0

        for interval in new_intervals:
            if interval.start < prev:
                return False
            prev = interval.end
        
        return True