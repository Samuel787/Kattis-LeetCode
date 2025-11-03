class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        prevColor = colors[0]
        prevIdx = 0
        for i in range(1, len(colors)):
            if colors[i] == prevColor:
                if neededTime[i] > neededTime[prevIdx]:
                    totalTime += neededTime[prevIdx]
                    prevIdx = i

                else:
                    totalTime += neededTime[i]
            else:
                prevColor = colors[i]
                prevIdx = i
        return totalTime