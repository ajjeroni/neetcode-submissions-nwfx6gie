class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        res = nums[0]
        for i in range(1, n):
            if nums[i] != res:
                count -= 1
            res = nums[i] if count == 0 else res
            count += 1
        return res