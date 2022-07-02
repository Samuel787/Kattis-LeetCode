class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        maxHeight = 0
        maxWidth = 0
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.insert(0, 0)
        verticalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        for i in range(1, len(horizontalCuts)):
            maxHeight = max(maxHeight, horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, len(verticalCuts)):
            maxWidth = max(maxWidth, verticalCuts[i] - verticalCuts[i - 1])
        return maxHeight * maxWidth % 1000000007