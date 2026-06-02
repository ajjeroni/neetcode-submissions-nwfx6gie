class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0

        summ = 0
        n = len(height)

        l, r = 0, n - 1
        maxL, maxR = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                summ += max(0, min(maxL,maxR) - height[l])
                l += 1
                maxL = max(maxL, height[l])
            else:
                summ += max(0, min(maxL,maxR) - height[r])
                r -= 1
                maxR = max(maxR, height[r])

        return summ