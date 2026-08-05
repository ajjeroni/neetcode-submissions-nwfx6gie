class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        l, r = 0, mountainArr.length() - 1
        while l < r:
            m = l + ((r - l) // 2)

            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak = l
        print(mountainArr.get(peak))

        l, r = 0, peak
        while l <= r:
            m = l + ((r - l) // 2)
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid < target:
                l = m + 1
            else:
                r = m - 1
        
        l, r = peak + 1, mountainArr.length() - 1
        while l <= r:
            m = l + ((r - l) // 2)
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid < target:
                r = m - 1
            else:
                l = m + 1
        return -1
