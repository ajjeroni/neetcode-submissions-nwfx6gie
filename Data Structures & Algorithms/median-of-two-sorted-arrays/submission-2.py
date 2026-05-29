class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # lets find the smallest array first
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        # nums2 is the smallest

        m = len(nums1)
        n = len(nums2)
        left, right = 0, n - 1
        half_total_len = (m + n) // 2

        while True:
            l2_index = (left + right) // 2
            l1_index = half_total_len - (l2_index + 1) - 1

            l1 = nums1[l1_index] if l1_index >= 0 else float('-inf')
            r1 = nums1[l1_index + 1] if l1_index + 1 < len(nums1) else float('inf')
            l2 = nums2[l2_index] if l2_index >= 0 else float('-inf')
            r2 = nums2[l2_index + 1] if l2_index + 1 < len(nums2) else float('inf') 

            if l1 > r2:
                left = l2_index + 1
            elif l2 > r1:
                right = l2_index - 1
            else:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return min(r1, r2)
