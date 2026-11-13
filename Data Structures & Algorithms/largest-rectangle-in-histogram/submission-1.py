class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                prev_i, prev_h = stack.pop()
                area = prev_h * (i - prev_i)
                maxArea = max(area, maxArea)
                start = prev_i
            
            stack.append((start, h))
        
        while stack:
            i, h = stack.pop()
            area = h * (len(heights) - i)
            maxArea = max(area, maxArea)
        
        return maxArea