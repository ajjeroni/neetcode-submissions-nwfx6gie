class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        O_of_1_searching_list = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in O_of_1_searching_list:
                nextNum = num + 1
                length = 1
                while nextNum in O_of_1_searching_list:
                    length += 1
                    nextNum += 1
                longest = max(longest, length)
        return longest
