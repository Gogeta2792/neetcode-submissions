class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if end < newStart:
                res.append(intervals[i])
            elif start > newEnd:
                res.append([newStart, newEnd])
                return res + intervals[i:]
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        
        res.append([newStart, newEnd])

        return res