class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            nums[0],nums[1] = nums[1],nums[0]
            return nums
        products = [0] * len(nums)
        pre = 1
        for i in range(len(nums)):
            products[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] *= post
            post *= nums[i]
        return products

