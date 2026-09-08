class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval[0], newInterval[1]
        left, right = len(intervals), len(intervals)

        for idx in range(len(intervals)):
            if newStart < intervals[idx][0]:
                left, right = idx, idx
                break
        
        while left > 0 and newStart <= intervals[left - 1][1]: #prev end
            left -= 1
        
        while right < len(intervals) and newEnd >= intervals[right][0]: #next start
            right += 1

        left_side = intervals[:left]
        middle = [newInterval] if left == right else [[min(newStart, intervals[left][0]), max(newEnd, intervals[right - 1][1])]]
        
        middle.extend(intervals[right:])
        left_side.extend(middle)

        return left_side