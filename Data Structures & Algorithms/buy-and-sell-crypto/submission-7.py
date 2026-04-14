class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = r = 0
        while r < len(prices):
            while prices[l] >= prices[r] and l < r:
                l += 1
            maxP = max(maxP, prices[r]-prices[l])

            r += 1
        return maxP