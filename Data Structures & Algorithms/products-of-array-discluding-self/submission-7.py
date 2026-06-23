class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # prefix
        # [1, 1, 2, 8]
        pre = 1
        for i in range(len(nums)):
            prefix[i] = pre
            pre *= nums[i]
        print(prefix)

        # suffix
        # [48, 24, 6, 1]
        suff = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = suff
            suff *= nums[i]
        print(suffix)

        res = [1] * len(nums)
        for i in range(len(res)):
            res[i] = prefix[i] * suffix[i]
        return res