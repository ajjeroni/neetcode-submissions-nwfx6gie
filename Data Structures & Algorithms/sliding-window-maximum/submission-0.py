from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l = r = 0
        maximums = []
        while r < len(nums):
            while dq and dq[-1][0] < nums[r]:
                dq.pop()
            dq.append((nums[r],r))
            if r-l+1 == k:
                if dq[0][1] < l:
                    dq.popleft()
                maximums.append(dq[0][0])
                l += 1 

            r += 1  
        return maximums