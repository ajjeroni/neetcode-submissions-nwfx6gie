class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1: return 0 if nums[0] == target else -1

        # find min first
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        if nums[r] > target: return -1
        if nums[r] == target: return r

        pivot = l
        l, r = 0, len(nums) - 1

        if nums[l] <= nums[r]:
            l, r = 0, len(nums) - 1
        elif nums[l] <= target <= nums[pivot - 1]:
            r = pivot - 1
        elif nums[pivot] < target <= nums[r]:
            l = pivot
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1









