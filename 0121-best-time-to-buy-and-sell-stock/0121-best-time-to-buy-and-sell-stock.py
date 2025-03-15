class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        currLow = prices[0]
        for price in prices:
            result = max(result, price - currLow)
            if price < currLow:
                currLow = price
        return result
