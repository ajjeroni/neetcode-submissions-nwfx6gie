class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0 
        L, R = 0, 1
        while R < len(prices):
            if prices[L] < prices[R]:
                prof = prices[R] - prices[L]
                maxProf = max(maxProf, prof)
            else:
                L = R
            R += 1
        return maxProf