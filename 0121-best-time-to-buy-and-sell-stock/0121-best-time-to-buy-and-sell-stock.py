class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = -1
        prev_min = prices[0]
        for price in prices:
            profit = max(profit, price - prev_min)
            prev_min = price if price < prev_min else prev_min
        return profit

        