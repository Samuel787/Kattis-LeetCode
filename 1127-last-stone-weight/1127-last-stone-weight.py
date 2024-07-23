class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        pq = []
        for stone in stones:
            pq.append(stone * -1)
        heapq.heapify(pq)

        while len(pq) > 0:
            largestStone = heapq.heappop(pq)
            if len(pq) == 0:
                return largestStone * -1
            secondLargestStone = heapq.heappop(pq)
            result = largestStone - secondLargestStone
            if result != 0:
                heapq.heappush(pq, result)
            
        return 0
        