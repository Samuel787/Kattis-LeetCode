class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        running_min = 10001
        maxProfit = 0
        for price in prices:
            currentProfit = price - running_min
            maxProfit = max(maxProfit, currentProfit)
            if price < running_min:
                running_min = price

        return maxProfit


        