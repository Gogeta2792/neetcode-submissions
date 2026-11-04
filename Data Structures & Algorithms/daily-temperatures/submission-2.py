class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and curr_temp > stack[-1][1]:
                idx, temp = stack.pop()
                res[idx] = curr_day - idx
            stack.append((curr_day, curr_temp))
        
        return res