class MedianFinder(object):

    def __init__(self):
        self.small_heap = [] # max heap
        self.large_heap = [] # min heap


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small_heap, num * -1)

        max_in_small = self.small_heap[0] * -1
        if len(self.large_heap) > 0:
            min_in_large = self.large_heap[0]

            # ensure heap partition
            if max_in_small > min_in_large:
                val = heapq.heappop(self.small_heap) * -1
                heapq.heappush(self.large_heap, val)
        
        
        # rebalance the heap
        while abs(len(self.small_heap) - len(self.large_heap)) > 1:
            if len(self.small_heap) > len(self.large_heap):
                val = heapq.heappop(self.small_heap) * -1
                heapq.heappush(self.large_heap, val)
            else:
                val = heapq.heappop(self.large_heap)
                heapq.heappush(self.small_heap, val * -1)

    def findMedian(self):
        """
        :rtype: float
        """
        # print("small heap: " + str(self.small_heap) + " and large heap: " + str(self.large_heap))
        if len(self.small_heap) == len(self.large_heap):
            max_in_small = self.small_heap[0] * -1
            min_in_large = self.large_heap[0]
            return (max_in_small + min_in_large) / 2.0
        elif len(self.small_heap) > len(self.large_heap):
            return self.small_heap[0] * -1
        else:
            if len(self.large_heap) > len(self.small_heap):
                return self.large_heap[0]
            else:
                return self.small_heap[0] * -1
            # return heapq.heapop(self.large_heap)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()