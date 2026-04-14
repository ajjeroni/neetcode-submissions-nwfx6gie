class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find_min(nums):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l

        def binary_search(l,r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        
        l,r = 0, len(nums) - 1
        min_i = find_min(nums)

        if min_i == 0:
            return binary_search(l,r)
        elif nums[min_i] <= target <= nums[r]:
            return binary_search(min_i, r)
        else:
            return binary_search(l, min_i - 1)

