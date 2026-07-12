from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        maxQue = deque()
        # monotonic decreasing queue
        # (int, index)
        
        while r < len(nums):
            
            while maxQue and maxQue[-1][0] <= nums[r]:
                maxQue.pop()

            maxQue.append((nums[r], r))

            if (r - l + 1) == k:
                while maxQue[0][1] < l:
                    maxQue.popleft()
                res.append(maxQue[0][0])
                l += 1

            r += 1
        return res

        # (1, 0)
        # -1
        # (1,0), (-1,1)





