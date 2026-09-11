class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = len(intervals), len(intervals)
        newStart, newEnd = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            if newStart < intervals[i][0]:
                left, right = i, i
                break
        
        while left > 0 and intervals[left - 1][1] >= newStart:
            left -= 1
        
        while right < len(intervals) and newEnd >= intervals[right][0]:
            right += 1
        
        merged = newInterval if left == right else [min(intervals[left][0], newStart), max(intervals[right - 1][1], newEnd)]

        return intervals[:left] + [merged] + intervals[right:]