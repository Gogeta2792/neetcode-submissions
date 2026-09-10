class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda i: i[0])
        prevStart, prevEnd = intervals[0][0], intervals[0][1]
        res = []

        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i][0], intervals[i][1]

            # There is overlap
            if prevEnd >= currStart: 
                prevStart = min(prevStart, currStart)
                prevEnd = max(prevEnd, currEnd)
                continue

            # There is no overlap
            else:
                res.append([prevStart, prevEnd])
                prevStart, prevEnd = currStart, currEnd
            
        res.append([prevStart, prevEnd])

        return res