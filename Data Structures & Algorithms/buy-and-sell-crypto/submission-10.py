class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        L, R = 0, 1
        while R < len(prices):
            if prices[L] > prices[R]:
                L = R
            else:
                currProf = prices[R] - prices[L]
                maxProf = max(maxProf, currProf)
            R += 1

        return maxProf