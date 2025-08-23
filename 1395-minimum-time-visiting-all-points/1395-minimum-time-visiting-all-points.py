class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        curr = points[0]
        time = 0
        for i in range(1, len(points)):
            target = points[i]
            # first we calculate the number of diagonal movements
            
            xSteps = abs(target[0] - curr[0])
            ySteps = abs(target[1] - curr[1])
            time += max(xSteps, ySteps)
            # second we calcualte the number of horizontal/vertical movements
            curr = target
        return time