from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxLen = 0
        l = r = 0
        maxDq = deque()
        minDq = deque()

        while r < len(nums):

            while maxDq and maxDq[-1] < nums[r]:
                maxDq.pop()
            maxDq.append(nums[r])

            while minDq and minDq[-1] > nums[r]:
                minDq.pop()
            minDq.append(nums[r])

            while maxDq[0] - minDq[0] > limit:
                if maxDq[0] == nums[l]:
                    maxDq.popleft()
                
                if minDq[0] == nums[l]:
                    minDq.popleft()

                l += 1
            
            maxLen = max(maxLen, r - l + 1)

            r += 1

        return maxLen







