class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n + 1)
        dp[0] = 0
        squares = [x * x for x in range(1, n + 1) if x * x <= n]
        for target in range(1, n + 1):
            for sq in squares:
                if sq > target:
                    break
                if dp[target - sq] + 1 < dp[target]:
                    dp[target] = dp[target - sq] + 1
        return dp[n]
        