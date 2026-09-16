class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval[0], newInterval[1]
        res = []

        for i in range(len(intervals)):
            currStart, currEnd = intervals[i][0], intervals[i][1]

            if newStart > currEnd:
                res.append(intervals[i])
            elif newEnd < currStart:
                res.append([newStart, newEnd])
                return res + intervals[i:]
            else:
                newStart = min(newStart, currStart)
                newEnd = max(newEnd, currEnd)

        res.append([newStart, newEnd])

        return res