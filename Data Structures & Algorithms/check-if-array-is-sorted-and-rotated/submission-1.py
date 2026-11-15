class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        pivot = False
        curr_max = float("-inf")

        for num in nums:
            if num < curr_max:
                if pivot == True:
                    return False
                pivot = True
            curr_max = num

        
        return True if pivot == False or nums[-1] <= nums[0] else False