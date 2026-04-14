class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxCon = 0
        w = len(heights) - 1
        L, R = 0, len(heights) - 1
        while L < R:
            con = min(heights[L], heights[R]) * w
            maxCon = max(maxCon, con)
            w -= 1
            if heights[L] < heights[R]:
                L += 1
            else: 
                R -= 1
        return maxCon