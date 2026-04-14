class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute force
        # trivial - iterate through and find minimum 
        # Time: O(n)
        # Space: O(1)

        # Optimal
        # when a sorted list is rotated - there is a pivot 
        # where left is max and right is min
        # we need to find the right of that pivot 
        # since the list is sorted we can do binary search to search for the pivot
        

        l,r = 0,len(nums)-1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                # pivot is in the right side
                l = m + 1
            else:
                # nums[m] <= nums[r] 
                # pivot is in the left side 
                r = m
        return nums[l]


