class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = [0 for i in range(n + 1)]
        if n > 0:
            self.dp[1] = 1
        if n > 1:
            self.dp[2] = 2
        return self.computeWays(n) 
    
    def computeWays(self, n):
        if n == 0:
            return 0
        if self.dp[n] != 0:
            return self.dp[n]
        self.dp[n] = self.computeWays(n - 1) + self.computeWays(n - 2)
        return self.dp[n]