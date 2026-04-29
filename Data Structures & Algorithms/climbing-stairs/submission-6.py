class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def topDown(i):
            if i <= 2:
                return i
            if i in cache:
                return cache[i]
            cache[i] = topDown(i - 1) + topDown(i - 2)
            return cache[i]

        return topDown(n)
        