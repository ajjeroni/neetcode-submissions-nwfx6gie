class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict:
                numDict[nums[i]] += 1
            else:
                numDict[nums[i]] = 1
        for val in numDict.values():
            if val > 1:
                return True
        return False