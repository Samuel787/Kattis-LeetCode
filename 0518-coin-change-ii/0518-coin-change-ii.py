class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins.append(0)
        coins.sort()
        dp = [[0 for j in range(amount + 1)] for i in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 1
                elif j < coins[i]:
                    dp[i][j] = dp[i - 1][j] # just copy the previous row because having a bigger coin value than j means that coin is useless
                else:
                    dp[i][j] = dp[i][j - coins[i]] + dp[i - 1][j] # (include coins[i] + exclude coins[i])
        return dp[len(coins) - 1][amount]



        