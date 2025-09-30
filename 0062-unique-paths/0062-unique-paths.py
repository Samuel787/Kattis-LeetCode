class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * m for _ in range(n)]
    
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i -1][j] + dp[i][j -1]
        return dp[n - 1][m -1]