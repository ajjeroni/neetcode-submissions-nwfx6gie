class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return len(nums)

        nums.sort()
        print(nums)

        maxx = 0
        count = 1
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == curr + 1:
                count += 1
                maxx = max(maxx, count)
            elif nums[i] == curr:
                continue
            else: 
                count = 1
            curr = nums[i]

        maxx = max(maxx, count)
        return maxx
