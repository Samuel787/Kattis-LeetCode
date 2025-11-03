class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        prevColor = colors[0]
        prevIdx = 0
        for i in range(1, len(colors)):
            if colors[i] == prevColor:
                # we need to tie break between them
                # print("Color at idx: " + str(i) + " same as idx: " + str(prevIdx))
                if neededTime[i] > neededTime[prevIdx]:
                    totalTime += neededTime[prevIdx]
                    # print("We add this time: " + str(neededTime[prevIdx]))
                    prevIdx = i

                else:
                    totalTime += neededTime[i]
                    print("We add this time: " + str(neededTime[i]))
            else:
                prevColor = colors[i]
                prevIdx = i
        return totalTime