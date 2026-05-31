class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)

        for i,num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue
            
            target = 0 - num
            l, r = i + 1, len(nums) - 1
            while l < r:
                left = nums[l]
                right = nums[r]
                summ = left + right
                if summ == target:
                    res.append([num,left,right])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif summ < target:
                    l += 1
                else:
                    r -= 1
        return res
