class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # lower bound
        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2

            if nums[m] >= target:
                r = m
            else:
                # nums[m] < target:
                l = m + 1
        
        return l 
