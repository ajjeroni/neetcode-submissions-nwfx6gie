class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        a, b = nums1, nums2
        len_a = len(a)
        len_b = len(b)
        total = len_a + len_b
        half = total // 2

        l, r = 0, len_a - 1
        print(a, l, r)
        while True:
            a_i = (l + r) // 2
            b_i = half - (a_i + 1) - 1

            aLeft = float('-inf') if a_i < 0 else a[a_i]
            aRight = float('inf') if len_a <= a_i + 1 else a[a_i + 1]

            bLeft = float('-inf') if b_i < 0 else b[b_i]
            bRight = float('inf') if len_b <= b_i + 1 else b[b_i + 1]

            if aLeft > bRight:
                r = a_i - 1
            elif bLeft > aRight:
                l = a_i + 1
            else:
                if total % 2 != 0:
                    return min(aRight, bRight)
                else:
                    return ((max(aLeft, bLeft) + min(aRight, bRight)) / 2.0)