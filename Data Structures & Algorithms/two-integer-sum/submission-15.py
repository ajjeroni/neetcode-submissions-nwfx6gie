class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        
        for i,num in enumerate(nums):
            comp = target - num
            if comp in numMap:
                return [numMap[comp], i]

            numMap[num] = i
        

