class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1 
            target = 0 - num
            while l < r:
                numSum = nums[l] + nums[r]
                if numSum < target:
                    l += 1
                elif target < numSum:
                    r -= 1
                else:
                    triplets.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                

        return triplets