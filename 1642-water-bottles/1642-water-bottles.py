class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drinkCount = 0
        emptyBottles = 0
        while True:
            totalBottles = numBottles + emptyBottles
            if totalBottles < numExchange:
                drinkCount += numBottles
                numBottles = 0
                break
            drinkCount += numBottles
            numBottles = totalBottles // numExchange
            emptyBottles = totalBottles % numExchange

        return drinkCount