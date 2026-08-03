class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(target):
            subArrays = 1
            count = 0

            for num in nums:
                if num > target:
                    return False

                count += num
                if count > target:
                    subArrays += 1
                    count = num

            return subArrays <= k

        l, r = max(nums), sum(nums)

        while l < r:
            m = l + ((r - l) // 2)    

            if canSplit(m):
                r = m
            else:
                l = m + 1
        
        return l

