class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def does_k_work(mid):
            total = 0
            for b in piles:
                total += math.ceil(b/mid)
            return True if total <= h else False
        l,r = 1,max(piles)
        while l < r:
            m = (l + r) // 2
            if not does_k_work(m):
                l = m + 1
            else:
                r = m
        return r