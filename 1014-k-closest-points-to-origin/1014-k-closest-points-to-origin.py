class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distMap = {}
        distHeap = []
        heapq.heapify(distHeap)
        for point in points:
            dist = (point[0] * point[0] + point[1] * point[1])
            if dist in distMap:
                distMap[dist].append(point)
            else:
                distMap[dist] = [point]
            if len(distHeap) < k:
                heapq.heappush(distHeap, dist * - 1)
            else:
                maxDist = heapq.heappop(distHeap)
                if (maxDist * -1) > dist:
                    heapq.heappush(distHeap, dist * -1)
                else:
                    heapq.heappush(distHeap, maxDist)
        
        result = []
        for dist in distHeap:
            point = distMap[dist * -1].pop()
            result.append(point)
        return result

        