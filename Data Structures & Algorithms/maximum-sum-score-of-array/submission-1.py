class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        result = float('-inf')

        for num in nums:
            prefix += num
            suffix = total - prefix + num

            result = max(result, prefix, suffix)

        return result
        