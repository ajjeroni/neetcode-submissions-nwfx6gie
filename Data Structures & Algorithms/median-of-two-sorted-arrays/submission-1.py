class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute Force Approach 
        # create a concatenated list of m + n 
        # sort it 
        # return median of even or odd list 
        # Space O(n + m)
        # Time O(m+n * log(n + m)) 

        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        n = len(nums1)
        m = len(nums2)
        half = (n + m) // 2
        left = 0
        right = n - 1

        while True:

            # calculate middle of first list
            i = (left + right) // 2
            # calculate middle second list based on first index
            j = half - (i + 1) - 1

            # calculate partition values 
            l1 = float('-inf') if i < 0 else nums1[i]
            r1 = float('inf') if i + 1 >= n else nums1[i + 1]
            l2 = float('-inf') if j < 0 else nums2[j]
            r2 = float('inf') if j + 1 >= m else nums2[j + 1]

            if l1 > r2:
                right = i - 1
            elif l2 > r1:
                left = i + 1
            else:
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return min(r1, r2)



