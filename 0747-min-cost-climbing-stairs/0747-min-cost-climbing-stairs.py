class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        totalCost = [0 for i in range(len(cost) + 1)]
        for i in range(2, len(cost) + 1):
            totalCost[i] = min(cost[i - 1] + totalCost[i - 1], cost[i - 2] + totalCost[i - 2])
        return totalCost[-1]
