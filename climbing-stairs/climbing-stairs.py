class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        dp.append(1)
        dp.append(2)
        n -= 1
        if n <= 1:
            return dp[n]
        counter = 2
        while counter <= n:
            dp.append(dp[counter - 1] + dp[counter - 2])
            counter += 1
        return dp[n]
        
        