class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        K, L, R = 1, 0, 1
        while R < len(nums):
            if nums[L] == nums[R]:
                R += 1
            else:
                nums[L + 1] = nums[R]
                L += 1
                R += 1
                K += 1
        return K
        


        
