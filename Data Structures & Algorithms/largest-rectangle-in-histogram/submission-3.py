class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                area = (i - idx) * height
                maxArea = max(area, maxArea)
                start = idx
            stack.append([start, h])
        
        while stack:
            i, h = stack.pop()
            area = (len(heights) - i) * h
            maxArea = max(area, maxArea)
        
        return maxArea