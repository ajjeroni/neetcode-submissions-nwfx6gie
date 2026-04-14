class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numDict = {}
        for i, n in enumerate(nums):
            if n in numDict:
                numDict[n] += 1
            else:
                numDict[n] = 1
        
        for i, num in enumerate(numDict):
            nums[i] = num
        return len(numDict)
