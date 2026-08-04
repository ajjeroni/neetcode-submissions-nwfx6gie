class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the correct partitions 
        # keep nums1 the shortest
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        total = m + n
        half = total // 2
        l, r = 0, m - 1

        #  [1|2]  total: 3  mid1: -1   L: 0       median: 2.0
        #   [|3]     half: 1     mid2: 0  R: -1
        # max of the left side
        while True:
            mid1 = l + ((r - l) // 2)
            mid2 = (half - mid1) - 2

            l1 = nums1[mid1] if mid1 >= 0 else float('-inf') 
            r1 = nums1[mid1 + 1] if mid1 + 1 < m else float('inf')

            l2 = nums2[mid2] if mid2 >= 0 else float('-inf')
            r2 = nums2[mid2 + 1] if mid2 + 1 < n else float('inf')

            if l1 > r2:
                r = mid1 - 1
            elif l2 > r1:
                l = mid1 + 1
            else:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return float(min(r1, r2))






