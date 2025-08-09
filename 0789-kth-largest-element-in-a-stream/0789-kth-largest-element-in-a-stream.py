class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.min_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.min_heap, num)
        
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """ 
        if len(self.min_heap) >= self.k and self.min_heap[0] >= val:
                return self.min_heap[0]
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)