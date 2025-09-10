class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        mHeap = []
        heapq.heapify(mHeap)
        # we want a max Heap
        for s in stones:
            heapq.heappush(mHeap, s * -1)
        
        while len(mHeap) > 1:
            first = heapq.heappop(mHeap)
            second = heapq.heappop(mHeap)
            heapq.heappush(mHeap, first - second)
        
        val = heapq.heappop(mHeap) * -1
        return val
