class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [i * - 1 for i in stones]
        heapify(stones)

        while len(stones) > 1:
          heaviest = heappop(stones)
          second_heaviest = heappop(stones)
          result = heaviest - second_heaviest
          heappush(stones, result)
        return stones[0] * -1
      
        