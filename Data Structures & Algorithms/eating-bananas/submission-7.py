class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def testRate(k):
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / k)
            return True if totalHours <= h else False

        # h - total hours 
        # k - bananas/hour - we want minimum 
        # min: 1, max: max(piles)
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if testRate(m):
                r = m
            else:
                l = m + 1
        return l


