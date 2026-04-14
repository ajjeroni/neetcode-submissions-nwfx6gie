class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                height = min(heights[i],heights[j])
                max_w = max(max_w, height * (j-i))
        return max_w
        