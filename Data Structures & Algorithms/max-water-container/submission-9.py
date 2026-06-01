class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            mxArea = max(mxArea, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return mxArea