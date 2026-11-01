class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        prefix = [0] * len(nums)
        pre = 0
        for i in range(len(prefix)):
            pre += nums[i]
            prefix[i] = pre
        
        suffix = [0] * len(nums)
        suf = 0
        for i in range(len(nums) - 1, -1, -1):
            suf += nums[i]
            suffix[i] = suf

        return max([max(prefix), max(suffix)])
        