class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        s = [-1 * stone for stone in stones]
        heapq.heapify(s)
        while len(s) > 1:
            one = heapq.heappop(s)
            two = heapq.heappop(s)
            res = one - two
            heapq.heappush(s, res)
        if len(s) == 0:
            return 0
        else:
            return -1 * heapq.heappop(s)