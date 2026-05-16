from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # length of res is (n - k) + 1, where n is the length of nums
        res = []
        l = r = 0
        dq = deque()

        while r < len(nums):
            # print(dq, "L: ", l)
            while dq and dq[-1][0] < nums[r]:
                dq.pop()
            dq.append((nums[r], r))
            # print(dq, "L: ", l)

            if r - l + 1 == k:
                res.append(dq[0][0])
                while dq and dq[0][1] <= l:
                    dq.popleft() 
                l += 1       

            r += 1

        return res