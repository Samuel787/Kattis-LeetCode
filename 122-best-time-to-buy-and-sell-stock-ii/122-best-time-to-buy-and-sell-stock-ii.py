class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        wallet = 0
        buy_price = -1
        for i in range(len(prices)):
            if i == (len(prices) - 1):
                # sell off the stock if holding
                if buy_price != -1:
                    wallet += prices[i]
                    buy_price = -1
            elif prices[i] > prices[i + 1]:
                # if holding stock, sell off the stock
                if buy_price != -1:
                    wallet += prices[i]
                    buy_price = -1
            elif prices[i] < prices[i + 1]:
                # if not holding, buy the stock
                if buy_price == -1:
                    wallet -= prices[i]
                    buy_price = prices[i]
        return max(wallet, 0)