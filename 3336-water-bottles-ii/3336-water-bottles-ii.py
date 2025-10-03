class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            emptyBottles -= numExchange # you change numExchange amount of emptyBottles
            emptyBottles += 1 # you exchange the empty bottle for full bottle
            result += 1 # drink the full bottle
            numExchange += 1 # the cost of exchange increments by 1
        return result

        