class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [[] for i in range(3)]
        for num in nums:
            buckets[num].append(num)
        
        i = 0
        for bucket in buckets:
            for num in bucket:
                nums[i] = num
                i += 1