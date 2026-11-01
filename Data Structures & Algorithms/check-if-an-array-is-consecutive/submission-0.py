class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        unique = set(nums)

        if len(unique) < len(nums): return False

        size = len(nums)

        for num in nums:
            if num - 1 in unique:
                continue
            
            for i in range(num, num + size):
                if i not in unique:
                    return False
        return True