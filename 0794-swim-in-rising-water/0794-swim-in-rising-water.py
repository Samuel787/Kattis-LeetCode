class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (grid[0][0], 0, 0))
        visited = set()

        while pq:
            h, r, c = heapq.heappop(pq)
            if (r, c) in visited:
                continue
            if r == n - 1 and c == n - 1:
                return h
            visited.add((r, c))
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + x, c + y
                if nr >= 0 and nr < n and nc >= 0 and nc < n:
                    max_elv = max(h, grid[nr][nc])
                    heapq.heappush(pq, (max_elv, nr, nc))
                
        return n - 1



    #     n = len(grid)
    #     low = grid[0][0]
    #     high = n * n - 1
    #     ans = n * n - 1
    #     self.n = n
    #     self.grid = grid
        
    #     while low <= high:
    #         t = (low + high) // 2
    #         if self.canReachBottomRight(t):
    #             ans = t
    #             high = t - 1
    #         else:
    #             low = t + 1
    #     return ans
    
    # def canReachBottomRight(self, t):

    #     visited = set()
    #     mQueue = [(0, 0)]

    #     while mQueue:
    #         r, c = mQueue.pop(0)
    #         if (r, c) in visited:
    #             continue
    #         if r == self.n - 1 and c == self.n -1:
    #             return True
            
    #         visited.add((r, c))
    #         for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
    #             nr, nc = r + x, c + y
    #             n = self.n
    #             if nr >= 0 and nr < n and nc >= 0 and nc < n and self.grid[nr][nc] <= t:
    #                 mQueue.append((nr, nc))
    #     return False
            