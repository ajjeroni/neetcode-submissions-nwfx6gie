class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = set()
        for i, num in enumerate(nums):
            poo = 0 - num 
            L, R = i + 1, len(nums) - 1
            while L < R:
                pee = nums[L] + nums[R]
                if pee == poo:
                    result.add(tuple([num, nums[L], nums[R]]))
                    L += 1
                    R -= 1
                if pee < poo:
                    L += 1
                if pee > poo:
                    R -= 1
        return list(result)


                