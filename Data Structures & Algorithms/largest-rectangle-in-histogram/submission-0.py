class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        n = len(heights)
        mA = 0

        for i,h in enumerate(heights):
            start = i
            while stk and h <= stk[-1][0]:
                bH, j = stk.pop()
                w = i - j
                a = bH * w
                mA = max(mA, a)
                print(mA)
                start = j
            stk.append((h, start))
            print(stk)

        for h, i in stk:
            w = n - i
            print('width:',w)
            print('height:',h)
            a = h * w
            mA = max(mA, a)
            print(mA)
        
        return mA
        
        