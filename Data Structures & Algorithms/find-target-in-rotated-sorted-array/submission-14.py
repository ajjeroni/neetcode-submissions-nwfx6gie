class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(s, e):
            l, r = s, e
            while l < r:
                m = l + (r - l) // 2
                if nums[r] < nums[m]:
                    l = m + 1
                else:
                    r = m
            return l

        def biSearch(s, e):
            l, r = s, e
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        l, r = 0, len(nums) - 1

        if nums[l] <= nums[r]:
            return biSearch(l, r)

        pivot = findMin(l, r)

        if nums[l] <= target <= nums[pivot - 1]:
            return biSearch(l, pivot - 1)
        elif nums[pivot] <= target <= nums[r]:
            return biSearch(pivot, r)
        else:
            return -1
        

















