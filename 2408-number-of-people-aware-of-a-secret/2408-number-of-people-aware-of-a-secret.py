class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [0 for _ in range(n + 1)]
        # dp[i] is the number of people who found the secret in day i
        dp[1] = 1

        share = 0
        for i in range(2, n + 1):
            # Add people who can start sharing today
            if i - delay > 0:
                share = (share + dp[i - delay]) % MOD

            if i - forget > 0:
                share = (share - dp[i - forget] + MOD) % MOD
            
            dp[i] = share
            

        total = 0
        for i in range(n - forget + 1, n + 1):
            total = (total + dp[i]) % MOD
        
        return total
        
