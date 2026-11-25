class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                idx, height = stack.pop()
                area = height * (i - idx)
                maxArea = max(area, maxArea)
                start = idx
            
            stack.append([start, h])
        
        while stack:
            i, h = stack.pop()
            area = h * (len(heights) - i)
            maxArea = max(area, maxArea)
        
        return maxArea