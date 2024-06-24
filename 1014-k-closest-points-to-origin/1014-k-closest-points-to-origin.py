class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        # a + b <= c

        distanceMap = {}
        manhattanArr = []

        for point in points:
            manhattanDist = point[0]**2 + point[1]**2
            if manhattanDist in distanceMap:
                distanceMap[manhattanDist].append(point)
            else:
                distanceMap[manhattanDist] = [point]
            manhattanArr.append(manhattanDist)

        manhattanArr.sort()

        result = []
        i = 0
        while i < k:
            dist = manhattanArr[i]
            pointsWithDist = distanceMap[dist]
            print(str(pointsWithDist))
            numPointsWithDist = len(pointsWithDist)

            requiredPoints = k - i
            print("requiredPoints: " + str(requiredPoints))
            if numPointsWithDist <= requiredPoints:
                for point in pointsWithDist:
                    result.append(point)
                i += numPointsWithDist
                print("value of i now is: " + str(i))
            else:
                for j in range(requiredPoints):
                    result.append(pointsWithDist[j])
                i = k
        return result
        