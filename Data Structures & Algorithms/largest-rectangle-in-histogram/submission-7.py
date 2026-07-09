class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][0] >= h:
                height, idx = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            
            stack.append((h, start))
        
        while stack:
            maxArea = max(maxArea, stack[-1][0] * (len(heights) - stack[-1][1]))
            stack.pop()

        return maxArea