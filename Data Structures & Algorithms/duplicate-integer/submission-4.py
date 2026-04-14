from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = Counter(nums)
        if len(numDict) < len(nums):
            return True
        return False