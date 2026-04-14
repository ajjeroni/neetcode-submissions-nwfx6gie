class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #lets get them postfixes
        ret = [1] * len(nums)
        post = 1
        for i in range(len(ret) - 1, -1, -1):
            ret[i] = post 
            post = post * nums[i]
        pre = 1
        for i in range(len(ret)):
            ret[i] = pre * ret[i]
            pre = pre * nums[i]
        return ret