class StockSpanner(object):

    def __init__(self):
        self.currentDay = 0
        self.stockPrices = []
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if self.currentDay == 0:
            self.stockPrices.append(price)
            self.stack.append(self.currentDay)
            self.currentDay += 1
            return 1
        
        while len(self.stack) > 0:
            if self.stockPrices[self.stack[-1]] <= price:
                self.stack.pop()
            else:
                break
        
        if len(self.stack) != 0:
            top = self.stack[-1]
            result = self.currentDay - top
        else:
            result = self.currentDay + 1
        self.stack.append(self.currentDay)
        self.stockPrices.append(price)
        self.currentDay += 1
        return result

        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)