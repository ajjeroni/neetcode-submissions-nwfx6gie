class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        # monotonic increasing stack
        for i,h in enumerate(heights):
            index = i
            maxArea = max(maxArea, h)
            while stack and stack[-1][0] >= h:
                index = stack[-1][1]
                maxArea = max(maxArea, ((i-index) * stack[-1][0]))
                stack.pop()
            
            stack.append((h,index)) 
        print(stack)
        while stack:
            area = (len(heights) - stack[-1][1]) * stack[-1][0]
            maxArea = max(maxArea,area)
            stack.pop()
        return maxArea