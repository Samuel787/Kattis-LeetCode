class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        profitArr = []
        for i in costs:
            profitArr.append((i[1] - i[0], i[0], i[1]))
        
        profitArr.sort()
        
        totalCost = 0
        length = len(costs)
        for i in range(len(profitArr)):
            if i < length / 2:
                # choose B
                totalCost += profitArr[i][2]
            else:
                totalCost += profitArr[i][1]
        return totalCost
        
        