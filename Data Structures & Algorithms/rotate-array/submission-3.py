class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        def revList(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k %= len(nums)
        
        revList(0, len(nums) - 1)
        revList(0, k - 1)
        revList(k, len(nums) - 1)

        
        