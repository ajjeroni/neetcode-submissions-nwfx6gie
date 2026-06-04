class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2 = m - 1, len(nums2) - 1
        w = len(nums1) - 1

        while n1 > -1 and n2 > -1:
            if nums1[n1] > nums2[n2]:
                nums1[w] = nums1[n1]
                n1 -= 1
            else:
                # nums1[n1] <= nums2[n2]
                nums1[w] = nums2[n2]
                n2 -= 1
            w -= 1
        
        while n2 > -1:
            nums1[w] = nums2[n2]
            n2 -= 1
            w -= 1
        
        
