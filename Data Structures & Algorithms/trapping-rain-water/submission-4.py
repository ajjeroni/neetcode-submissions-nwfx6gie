class Solution:
    def trap(self, height: List[int]) -> int:
        L,R = 0, len(height) - 1
        mL, mR = height[L], height[R]
        tW = 0
        while L < R:
            if mL <= mR:
                L += 1
                mL = max(mL, height[L])
                tW += mL - height[L]
            else:
                R -= 1
                mR = max(mR, height[R])
                tW += mR - height[R]
        return tW