class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: 
                # Once we hit the point of the next "higher temperature" day
                t, i = stack.pop()
                res[i] = idx - i # we can do this because we know that otherwise it would be 0 at res[i]
            stack.append((temp,idx))

        return res