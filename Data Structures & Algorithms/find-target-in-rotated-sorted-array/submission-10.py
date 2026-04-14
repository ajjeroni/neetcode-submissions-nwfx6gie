class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(l,r):
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    # nums[m] <= nums[r]
                    r = m
            return r
        def bSearch(l,r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        l,r = 0,len(nums)-1
        pivot = findMin(l,r)
        if nums[l] <= nums[r]:
            return bSearch(l,r)
        elif nums[pivot] <= target and target <= nums[r]:
            return bSearch(pivot,r)
        else:
            return bSearch(l,pivot-1)
            
