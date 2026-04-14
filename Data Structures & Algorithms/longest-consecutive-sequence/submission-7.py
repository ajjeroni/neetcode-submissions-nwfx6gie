class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #check if num - 1 exists

        setNums = set(nums)
        longest = 0

        for num in nums:
            length = 0
            if num - 1 not in setNums:
                length += 1
                nextNum = num + 1
                while nextNum in setNums:
                    length += 1
                    nextNum += 1
            longest = max(length, longest)
        return longest
