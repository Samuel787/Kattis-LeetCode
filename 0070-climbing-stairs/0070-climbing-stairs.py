class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        count = 0
        cache = [0 for i in range(n + 1)]
        cache[0] = 0
        cache[1] = 1
        cache[2] = 2
        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]
        
