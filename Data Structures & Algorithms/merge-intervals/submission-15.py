class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda i: i[0])
        merged = []
        
        prevStart, prevEnd = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i][0], intervals[i][1]

            # no overlap
            if currStart > prevEnd:
                merged.append([prevStart, prevEnd])
                prevStart, prevEnd = currStart, currEnd

            # overlap
            else:
                prevStart, prevEnd = min(prevStart, currStart), max(prevEnd, currEnd)
            
        merged.append([prevStart, prevEnd])

        return merged