# from collections import defaultdict
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen = {}
        idx = 0

        for i,num in enumerate(nums):
            if num != val:
               seen[idx] = num
               idx += 1

        for i in range(idx):
            nums[i] = seen[i]
        
        return idx