class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict:
                return True
            else:
                numDict[nums[i]] = 1
        return False