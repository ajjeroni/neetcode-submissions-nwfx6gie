class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxProf = 0
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxProf = max(maxProf, profit)
            else:
                L = R
            R += 1
        return maxProf

        