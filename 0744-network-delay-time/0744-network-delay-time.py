class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adjList = {}
        for i in range(1, n + 1):
            adjList[i] = set()
        for edge in times:
            u, v, w = edge
            adjList[u].add((v, w))
        # print("This is my adjList: " + str(adjList))
        
        distArr = [float('inf') for _ in range(n + 1)]
        distArr[0] = 0
        distArr[k] = 0

        pq = [(0, k)]
        heapq.heapify(pq)
        visited = set()

        while pq:
            top = heapq.heappop(pq)
            src = top[1]
            if src in visited:
                continue
            distArr[src] = top[0]
            for edge in adjList[src]:
                print("inside for loop")
                timeToReachSrc = top[0]
                timeToReachDest = edge[1] # from src
                dest = edge[0]
                heapq.heappush(pq, (timeToReachSrc + timeToReachDest, dest))
                # print("This is my heapq: " + str(pq))
            visited.add(src)
            if len(visited) == n:
                return max(distArr)
        return -1

        