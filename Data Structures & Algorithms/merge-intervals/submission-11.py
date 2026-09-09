class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda interval: interval[0])
        prevStart, prevEnd = sorted_intervals[0][0], sorted_intervals[0][1]

        merged = []

        for i in range(1, len(sorted_intervals)):
            currStart, currEnd = sorted_intervals[i][0], sorted_intervals[i][1]

            if  prevEnd >= currStart: # There is overlap, hence update the prev accordingly
                prevStart = min(prevStart, currStart)
                prevEnd = max(prevEnd, currEnd)
                continue

            merged.append([prevStart, prevEnd])
                
            prevStart, prevEnd = currStart, currEnd
        
        merged.append([prevStart, prevEnd])
                
        
        return merged