class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                idx, h = stack.pop()
                area = h * (i - idx)
                maxArea = max(maxArea, area)
                start = idx
            stack.append((start, height))
        
        while stack:
            i, h = stack.pop()
            area = (len(heights) - i) * h
            maxArea = max(maxArea, area)
        
        return maxArea