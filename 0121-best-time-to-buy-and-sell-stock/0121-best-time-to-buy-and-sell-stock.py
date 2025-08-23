class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] -  buy)
            buy = min(buy, prices[i])
        return maxProfit
