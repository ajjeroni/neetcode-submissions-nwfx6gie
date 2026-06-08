class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = [0] * len(nums)
        
        for i,num in enumerate(nums):
            index = (i + k) % len(nums)
            copy[index] = num

        for i,num in enumerate(copy):
            nums[i] = num
        
        