class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i,num in enumerate(nums):
            left = 1
            for l in range(i):
                left *= nums[l]
            right = 1
            for r in range(i+1,len(nums)):
                right *= nums[r]
            res[i] = right * left
        return res