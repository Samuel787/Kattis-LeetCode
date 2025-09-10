class MedianFinder(object):

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # we add it first and then we rebalance the heaps
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
        elif num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, num * -1)
        
        # rebalancing
        while abs(len(self.minHeap) - len(self.maxHeap)) >= 2:
            if len(self.minHeap) > len(self.maxHeap):
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, val * -1)
            else:
                val = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, val * -1)

    def findMedian(self):
        """
        :rtype: float
        """
        # print("This is the maxHeap: " + str(self.maxHeap))
        # print("This is the minHeap: " + str(self.minHeap))
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return self.maxHeap[0] * -1
        else:
            # print("it is here")
            return (self.minHeap[0] + self.maxHeap[0] * -1) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()