class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # two pointer approach 

        if x >= arr[-1]:
            return arr[-k:]

        if x <= arr[0]:
            return arr[:k]
        
        l, r = 0, len(arr) - 1

        while l <= r and (r - l + 1) > k:
            left = abs(arr[l] - x)
            right = abs(arr[r] - x)

            if right < left:
                l += 1
            else:
                # right >= left
                r -= 1
        
        return arr[l:r+1]










