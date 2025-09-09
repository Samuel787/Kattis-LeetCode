class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        dp.append(1)
        dp.append(2)
        if n <= 2:
            return dp[n-1]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]
        
