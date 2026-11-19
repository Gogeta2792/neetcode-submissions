class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval

        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_end < start:
                res.append(intervals[i])
            elif end < curr_start:
                res.append([start,end])
                return res + intervals[i:]
            
            else:
                start = min(start, curr_start)
                end = max(end, curr_end)
        
        res.append([start, end])
        return res