class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        res = 1001
        while L <= R:
            M = (L + R) // 2
            res = min(res, nums[M])

            if nums[L] < nums[R]:
                res = min(res, nums[L])
            
            if nums[L] <= nums[M]:
                L = M + 1
            elif nums[M] < nums[R]:
                R = M - 1

        return res