class Solution(object):
    
    dp = [1, 2]
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= len(self.dp):
            return self.dp[n - 1]
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        for i in range(len(self.dp), n, 1):
            self.dp.append(0)
        self.dp[n - 1] = result
        return self.dp[n-1]
        
        
        