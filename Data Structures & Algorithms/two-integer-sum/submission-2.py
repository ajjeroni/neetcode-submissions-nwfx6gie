class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            numDict[nums[i]] = i 
        print(numDict)
        for i in range(len(nums)):
            pair = target - nums[i]
            print(target, "=", pair, nums[i])
            if pair in numDict and i != numDict[pair]:
                return [i, numDict[pair]]
                