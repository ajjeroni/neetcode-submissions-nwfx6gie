class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in nums:
            prev = num - 1
            if prev not in s:
                length = 1
                nextNum = num + 1
                while nextNum in s:
                    length += 1
                    nextNum += 1
                longest = max(longest, length)
            else:
                continue 
        return longest