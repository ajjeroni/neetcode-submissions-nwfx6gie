class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastResults = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in pastResults:
                return [pastResults[diff], i]
            pastResults[n] = i
        