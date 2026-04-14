class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        results = set()
        for i, num in enumerate(nums):
            if num > 0:
                break 
            if i > 0 and num == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            comp = 0 - num
            while L < R:
                if nums[L] + nums[R] < comp:
                    L += 1
                elif nums[L] + nums[R] > comp:
                    R -= 1
                else:
                    results.add(tuple([num, nums[L], nums[R]]))
                    L += 1
                    R -= 1
        return list(results)