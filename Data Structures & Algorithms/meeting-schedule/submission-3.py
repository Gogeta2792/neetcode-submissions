"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key = lambda i: i.start)
        prev_end = -1
        for interval in sorted_intervals:
            if interval.start < prev_end:
                return False
            prev_end = interval.end
        
        return True