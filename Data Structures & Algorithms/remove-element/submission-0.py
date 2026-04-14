class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        K, L, R = 0, 0, 0
        while R < len(nums):
            if nums[R] == val:
                R += 1
            else:
                nums[L] = nums[R]
                L += 1
                R += 1
                K += 1
        return K



            
        