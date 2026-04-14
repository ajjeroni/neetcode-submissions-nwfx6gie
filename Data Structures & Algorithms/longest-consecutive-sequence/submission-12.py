class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        #O(N) for both space and time
        longest = 0
        for num in nums:
            if num - 1 not in unique:
                length = 1
                nextNum = num + 1
                while nextNum in unique:
                    length += 1   
                    nextNum += 1
                longest = max(longest, length)
        return longest