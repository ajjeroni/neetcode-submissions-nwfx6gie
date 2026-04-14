class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #use 2 pointer algorithm 
        #(j - i) * min(heights[i], heights[j])
        left, right, maxArea = 0, len(heights) - 1, 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            print("area:", area)
            maxArea = max(maxArea, area)
            print("max area:", maxArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return(maxArea)
            
