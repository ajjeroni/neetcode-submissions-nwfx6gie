class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l, r = 0, len(nums) - 1
        while l < r:
            if l > 0:
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            if r < len(nums) - 1:
                while nums[r] == nums[r + 1] and l < r:
                    r -= 1
            #what do you even call sum here?
            currSum = nums[l] + nums[r]
            if currSum == target:
                return [l+1,r+1]
            elif currSum < target:
                l += 1
            else:
                r -= 1
                