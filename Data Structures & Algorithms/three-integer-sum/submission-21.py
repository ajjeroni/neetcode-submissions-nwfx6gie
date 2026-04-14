class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n^3 brute approach 
        # we can use 2 sum approach which brings it down to n^2
        # we need to sort it first which is n log n
        # overall n^2
        nums.sort()
        sums = []
        for i,num in enumerate(nums):
            if num > 0:
                break 
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            l, r = i + 1, len(nums) - 1
            target = 0 - num
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum == target:
                    sums.append([num,nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                if currSum < target:
                    l += 1
                else:
                    r -= 1
        return sums
                





