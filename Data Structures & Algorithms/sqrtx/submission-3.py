class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r -l) // 2)
            sqrd = m ** 2
            if sqrd == x:
                return m
            elif sqrd < x:
                l = m + 1
                res = m
            else:
                # sqrd > x:
                r = m - 1
        
        return res