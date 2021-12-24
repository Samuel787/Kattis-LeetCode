class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minimum = 10001
        for i in prices:
            if i - minimum > profit:
                profit = i - minimum
            if i < minimum:
                minimum = i
        return profit