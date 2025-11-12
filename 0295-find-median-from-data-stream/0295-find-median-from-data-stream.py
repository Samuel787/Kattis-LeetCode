class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # used to store lower values
        self.minHeap = [] # used to store upper values

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
            return
        
        # rebalancing algo
        if len(self.maxHeap) == len(self.minHeap):
            if num >= self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, num * -1)
        else:
            odd = None
            if len(self.maxHeap) > len(self.minHeap):
                odd = heapq.heappop(self.maxHeap) * -1
            else:
                odd = heapq.heappop(self.minHeap)
            
            if num < odd:
                heapq.heappush(self.maxHeap, num * -1)
                heapq.heappush(self.minHeap, odd)
            else:
                heapq.heappush(self.minHeap, num)
                heapq.heappush(self.maxHeap, odd * -1)

        # print("This is minHeap: " + str(self.minHeap) + " and this is maxHeap: " + str(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            top = self.maxHeap[0] * -1
            # print("First top value is: " + str(top))
            top += self.minHeap[0]
            # print("now top value is: " + str(top))
            # print()
            return top / 2.0
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        else:
            return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()