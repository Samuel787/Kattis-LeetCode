class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.maxHeap = [-1 * num for num in nums]
        self.k = k
        heapq.heapify(self.maxHeap)
        self.minHeap = []

        # we maintain size of minHeap as k - 1. So Kth Largest element can be found in the maxHeap
        for i in range(k - 1):
            res = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, res * -1)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.minHeap) == 0 and self.k == 1:
            heapq.heappush(self.maxHeap, val * -1)    
        else:
            topOfMinHeap = heapq.heappop(self.minHeap)
            if val > topOfMinHeap:
                heapq.heappush(self.maxHeap, topOfMinHeap * -1)
                heapq.heappush(self.minHeap, val)   
            else:
                heapq.heappush(self.maxHeap, val * -1)
                heapq.heappush(self.minHeap, topOfMinHeap)
        
        return self.maxHeap[0] * -1
        



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)