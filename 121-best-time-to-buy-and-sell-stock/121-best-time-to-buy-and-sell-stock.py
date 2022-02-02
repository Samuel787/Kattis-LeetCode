class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) < 2:
            return max_profit
        left = 0
        for right in range(1, len(prices)):
            curr_profit = prices[right] - prices[left]
            max_profit = max(curr_profit, max_profit)
            if prices[right] < prices[left]:
                left = right
        return max_profit