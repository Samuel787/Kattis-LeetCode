class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        heapq.heapify(heap)

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                top = heapq.heappop(heap)
                if num > top:
                    heapq.heappush(heap, num)
                else:
                    heapq.heappush(heap, top)
        
        return heapq.heappop(heap)
                