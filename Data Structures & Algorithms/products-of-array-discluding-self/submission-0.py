class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 4, 6]
        #[48, 24, 12, 8]
        #[1, 1, 2, 8] left side 
        #[48, 24, 6, 1] right side
        results = [0] * len(nums) 
        prefix = 1
        for i in range(len(nums)):
            results[i] = prefix
            prefix *= nums[i]
        print(results)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= postfix
            postfix *= nums[i]
        return results