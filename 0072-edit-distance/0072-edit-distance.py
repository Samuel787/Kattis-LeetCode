class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        rows = len(word1)
        cols = len(word2)

        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        # we initialize the base cases
        for row in range(rows + 1):
            dp[row][cols] = rows - row
        for col in range(cols + 1):
            dp[row][col] = cols - col
        
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, - 1, -1):
                if word1[row] == word2[col]:
                    dp[row][col] = dp[row + 1][col + 1]
                else:
                    insertCount = dp[row][col + 1] + 1
                    deleteCount = dp[row + 1][col] + 1
                    replaceCount = dp[row + 1][col + 1] + 1
                    dp[row][col] = min(insertCount, deleteCount, replaceCount)
        
        return dp[0][0]