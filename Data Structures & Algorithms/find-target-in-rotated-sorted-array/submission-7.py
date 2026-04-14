class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and target == nums[0]:
            return 0

        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        min_i = r
        
        if min_i == 0:
            l, r = 0, n - 1
        elif nums[0] <= target and target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i, n - 1

        while l <= r:
            m = (l+r) // 2
            if target < nums[m]:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
 
        