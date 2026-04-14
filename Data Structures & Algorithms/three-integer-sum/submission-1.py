class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # O(nlogn)
        print(nums)

        result = set()
        for i, num in enumerate(nums):
        # O(n)
            L, R = i + 1, len(nums) - 1
            comp = 0 - num
            while L < R:
                if nums[L] + nums[R] == comp:
                    result.add(tuple([num, nums[L], nums[R]]))
                    L += 1
                    R -= 1
                elif nums[L] + nums[R] < comp:
                    L += 1
                elif nums[L] + nums[R] > comp:
                    R -= 1
        return list(result)
                     

