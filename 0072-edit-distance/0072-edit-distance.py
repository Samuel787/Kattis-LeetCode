class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        rows = len(word1) + 1
        cols = len(word2) + 1
        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j -1]:
                    dp[i][j] = dp[i - 1][j -1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j -1]) + 1
        return dp[rows - 1][cols - 1]