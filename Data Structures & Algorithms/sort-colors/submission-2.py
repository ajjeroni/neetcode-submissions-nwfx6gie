class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, read = 0, len(nums) - 1, 0

        while read <= r:
            if nums[read] == 0:
                nums[l], nums[read] = nums[read], nums[l]
                l += 1
            elif nums[read] == 2:
                nums[r], nums[read] = nums[read], nums[r]
                r -= 1
                read -= 1
            read += 1
        