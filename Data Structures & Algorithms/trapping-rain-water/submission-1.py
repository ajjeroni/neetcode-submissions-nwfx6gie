class Solution:
    def trap(self, height: List[int]) -> int:
        tWater = 0
        lMax = [0] * len(height)
        l = 0
        rMax = [0] * len(height)
        r = 0
        for i in range(len(height)):
            j = -i - 1
            lMax[i] = l
            l = max(l, height[i])
            rMax[j] = r
            r = max(r, height[j])
        for h in range(len(height)):
            tWater += max(0, (min(lMax[h], rMax[h]) - height[h]))
        return tWater