class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0 
        l = 0
        r = len(height) - 1
        lMax = height[l]
        rMax = height[r]
        while l < r:
            if height[l] < height[r]:
                lMax = max(lMax, height[l])
                water += lMax - height[l]
                l += 1
            else:
                rMax = max(rMax, height[r])
                water += rMax - height[r]
                r -= 1
        return water