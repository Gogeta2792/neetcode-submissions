class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = []
        prevStart, prevEnd = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i][0], intervals[i][1]

            if prevEnd >= curStart:
                prevEnd = max(prevEnd, curEnd)
            else:
                res.append([prevStart, prevEnd])
                prevStart, prevEnd = curStart, curEnd
            
        res.append([prevStart, prevEnd])
        return res