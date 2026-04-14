class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i, num in enumerate(nums):
            if 0 < num:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            comp = 0 - num
            while L < R:
                diff = nums[L] + nums[R]
                if comp == diff:
                    result.add(tuple([num, nums[L], nums[R]]))
                    L += 1
                    R -= 1
                elif diff < comp:
                    L += 1
                elif diff > comp:
                    R -= 1
        return list(result)