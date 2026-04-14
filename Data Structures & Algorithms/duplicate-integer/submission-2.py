class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compareSet = set(nums)
        if len(nums) > len(compareSet):
            return True
        return False