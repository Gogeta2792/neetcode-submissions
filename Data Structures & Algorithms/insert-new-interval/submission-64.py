class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval[0], newInterval[1]
        res = []

        for i in range(len(intervals)):
            curStart, curEnd = intervals[i][0], intervals[i][1]

            if curEnd < newStart:
                res.append(intervals[i])
            elif newEnd < curStart:
                res.append([newStart, newEnd])
                return res + intervals[i:]
            else:
                newStart = min(newStart, curStart)
                newEnd = max(newEnd, curEnd)
            
        res.append([newStart, newEnd])
        return res