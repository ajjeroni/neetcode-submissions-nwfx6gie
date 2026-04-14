class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        tWater = 0
        while l < r:
            if lMax <= rMax:
                l += 1
                lMax = max(lMax, height[l])
                tWater += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                tWater += rMax - height[r]
        return tWater