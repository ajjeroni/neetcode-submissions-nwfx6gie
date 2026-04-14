class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #maxWater = maxHeight * maxWidth
        #we need a max area var
        #two pointer approach 
        
        L, R = 0, len(heights) - 1
        area = 0
        width = len(heights) - 1

        while L < R:
            area = max(area, min(heights[L], heights[R]) * width)
            if heights[L] <= heights[R]:
                L += 1
                width -= 1
            elif heights[L] > heights[R]:
                R -= 1
                width -= 1
        return area