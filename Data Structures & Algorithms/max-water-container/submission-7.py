class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1
        while l < r:
            currArea = (r-l) * min(heights[l],heights[r])
            maxWater = max(maxWater,currArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater