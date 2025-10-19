class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - lowest)
            if prices[i] < lowest:
                lowest = prices[i]
        return maxProfit
        