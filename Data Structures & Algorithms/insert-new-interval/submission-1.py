class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval[0], newInterval[1]
        left, right = len(intervals), len(intervals)

        for idx, interval in enumerate(intervals):
            if newStart < interval[0]:
                left, right = idx, idx
                break

        while left > 0 and newStart <= intervals[left - 1][1]:
            left -= 1

        while right < len(intervals) and newEnd >= intervals[right][0]:
            right += 1
        
        left_list = intervals[:left]
        mid_list = [newInterval] if left == right else [[min(intervals[left][0], newStart), max(intervals[right - 1][1], newEnd)]]
        right_list = intervals[right:]

        mid_list.extend(right_list)
        left_list.extend(mid_list)

        return left_list