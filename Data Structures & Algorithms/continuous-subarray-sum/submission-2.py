class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1: return False

        seen = { 0 : -1 }
        total = 0

        for i,num in enumerate(nums):
            total += num
            remainder = total % k 
            
            # keep the earlist index of the remainder
            # even if remainder is the same skip it after the first occurence
            if remainder not in seen:
                seen[remainder] = i
            elif i - seen[remainder] > 1:
                return True

        return False