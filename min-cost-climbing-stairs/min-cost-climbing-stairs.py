class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.cost = cost
        self.dp = [None for i in range(len(cost))]
        return min(self.getMinCost(0), self.getMinCost(1))
          
    def getMinCost(self, index):
        if index >= len(self.cost):
            return 0
        if self.dp[index] != None:
            return self.dp[index]
        curr_cost = self.cost[index] + min(self.getMinCost(index + 1), self.getMinCost(index + 2))
        self.dp[index] = curr_cost
        return curr_cost