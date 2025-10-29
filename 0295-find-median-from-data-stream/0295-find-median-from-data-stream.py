class MedianFinder(object):

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
        elif num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, num * -1)

        # rebalance
        if len(self.minHeap) > len(self.maxHeap) + 1:
            top = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, top * - 1)

        elif len(self.maxHeap) > len(self.minHeap) + 1:
            top = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, top)


    def findMedian(self):
        """
        :rtype: float
        """

        # print("MinHeap: " + str(self.minHeap) + " maxHeap: " + str(self.maxHeap))
        if len(self.minHeap) == len(self.maxHeap):
            
            return (self.minHeap[0] + self.maxHeap[0] * -1) / 2.0
        
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return self.maxHeap[0] * -1

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()