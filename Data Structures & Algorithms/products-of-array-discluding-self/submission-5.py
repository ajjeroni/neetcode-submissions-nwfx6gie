class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)
        #find prefix 
        pre = 1
        for i in range(len(nums)):
            products[i] = pre
            pre *= nums[i]
        print(products)
        #multiply with post
        post = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] *= post
            post *= nums[i]
        print(products)
        return products