class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        unique = set(nums)

        if len(unique) < len(nums): return False

        size = len(nums)
        smallest = min(nums)

        for i in range(smallest + 1, smallest + size):
            if i not in unique: return False
        
        return True