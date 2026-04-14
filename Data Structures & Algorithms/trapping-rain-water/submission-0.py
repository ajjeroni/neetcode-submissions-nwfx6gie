class Solution:
    def trap(self, height: List[int]) -> int:
        lMax, rMax = height[0], height[-1]
        tWater = 0
        L, R = 0, len(height) - 1
        while L < R:
            if lMax <= rMax:
                L += 1
                lMax = max(lMax, height[L])
                tWater += lMax - height[L]
            else:
                R -= 1
                rMax = max(rMax, height[R])
                tWater += rMax - height[R]
        return tWater

