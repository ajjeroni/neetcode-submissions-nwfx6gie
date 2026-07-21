class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        l = r = 0
        length = float('inf')

        while r < len(nums):
            count += nums[r]
            
            while l <= r and count >= target:
                length = min(length, r - l + 1)

                count -= nums[l]
                l += 1

            r += 1

        return 0 if length == float('inf') else length