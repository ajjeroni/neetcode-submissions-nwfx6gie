class Solution:
    def trap(self, height: List[int]) -> int:
        summ = 0
        n = len(height)

        for i in range(1, n - 1):
            maxL = 0
            for j in range(i):
                maxL = max(maxL, height[j])

            maxR = 0
            for j in range(i + 1, n):
                maxR = max(maxR, height[j])

            summ += max(0, min(maxL,maxR) - height[i])
        
        return summ