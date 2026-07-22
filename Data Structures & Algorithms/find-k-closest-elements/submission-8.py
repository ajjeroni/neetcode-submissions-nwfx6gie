class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x >= arr[-1]:
            return arr[-k:]

        if x <= arr[0]:
            return arr[:k]
        
        l, r = 0, len(arr) - 1

        while l < r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            else:
                r = m 

        l = l - k

        if l < 0:
            l = 0
            r = k

        left = abs(arr[l] - x)
        nextRight = abs(arr[r] - x) if r < len(arr) else float('inf')

        while r < len(arr) and nextRight < left:
            l += 1
            r += 1
            left = abs(arr[l] - x)
            nextRight = abs(arr[r] - x) if r < len(arr) else float('inf')

        return arr[l:l+k]

