class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # convert everything to int
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])

        res = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    continue
                value = 1 + min(
                    matrix[i - 1][j],
                    matrix[i - 1][j - 1],
                    matrix[i][j - 1]
                )
                res = max(value, res)
                matrix[i][j] = value
        
        if res == 0:
            for i in range(rows):
                if matrix[i][0] == 1:
                    res = 1
                    break
        
        if res == 0:
            for i in range(cols):
                if matrix[0][i] == 1:
                    res = 1
                    break
        
        return res ** 2