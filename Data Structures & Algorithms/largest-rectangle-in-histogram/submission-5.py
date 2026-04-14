class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            maxArea = max(maxArea, h)
            index = i
            while stack and stack[-1][0] >= h:
                index = stack[-1][1]
                maxArea = max(maxArea, (i - index) * stack[-1][0])
                stack.pop()
            stack.append((h,index))
        print(stack)

        while stack:
            area = stack[-1][0] * (len(heights) - stack[-1][1])
            maxArea = max(maxArea,area)
            stack.pop()
        return maxArea


