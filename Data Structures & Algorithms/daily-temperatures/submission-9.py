class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for curr_i, curr_t in enumerate(temperatures):
            while stack and curr_t > stack[-1][1]:
                i, t = stack.pop()
                result[i] = curr_i - i
            stack.append((curr_i, curr_t))
        
        return result