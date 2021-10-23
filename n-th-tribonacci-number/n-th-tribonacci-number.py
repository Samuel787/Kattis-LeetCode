class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 1]
        for i in range(3, n + 1, 1):
            dp.append(dp[i-1] + dp[i - 2] + dp[i - 3])
        return dp[n]
        