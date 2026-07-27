class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def test_k(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            return h >= hours

        n = max(piles)
        L, R = 1, n

        while L < R:
            M = L + ((R - L) // 2)

            if test_k(M):
                R = M
            else:  
                L = M + 1
        
        return R