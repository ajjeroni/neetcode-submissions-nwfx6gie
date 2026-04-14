class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        r = 1
        l = max_p = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                max_p = max(max_p, (prices[r] - prices[l]))
            r += 1
        return max_p
