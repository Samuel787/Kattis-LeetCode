class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        heap = []
        heapq.heapify(heap)
        for i in range(len(heights) - 1):
            if heights[i + 1] <= heights[i]:
                continue
            diff = heights[i + 1] - heights[i]
            # assert diff is positive
            if diff <= bricks:
                bricks -= diff
                heapq.heappush(heap, -1 * diff)
            elif ladders > 0:
                if len(heap) > 0:
                    salvage = heap[0] * -1
                    if salvage > diff:
                        bricks += salvage
                        heapq.heappop(heap)
                        heapq.heappush(heap, diff * -1)
                        bricks -= diff
                ladders -= 1
            else:
                return i
        return len(heights) -1
            
                
                
                
                        
                