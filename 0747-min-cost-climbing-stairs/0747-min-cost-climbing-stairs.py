class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        costArr = [-1 for i in cost]
    
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        costArr[0] = 0
        costArr[1] = 0

        for i in range(len(cost)):
            if i < 2:
                continue
            costArr[i] = min(costArr[i - 1] + cost[i - 1], costArr[i - 2] + cost[i - 2])
            print("cost to come to step " + str(i) + " costs " + str(costArr[i]))
        
        return min(costArr[-1] + cost[-1], costArr[-2] + cost[-2])
            