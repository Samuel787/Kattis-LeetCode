class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """ 
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.matrix = matrix
        self.cache = {}
        total = 0
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = 1 + min(
                    matrix[i - 1][j],
                    matrix[i - 1][j - 1],
                    matrix[i][j - 1]
                )
                total += matrix[i][j]
        # count the number of 1s in the first row
        for i in range(self.cols):
            total += matrix[0][i]
        # count the number of 1s in the first col
        for i in range(self.rows):
            total += matrix[i][0]

        total -= matrix[0][0]

        return total


    #     total = 0
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             total += self.dfs(i, j)
        
    #     return total
        
    # def dfs(self, row, col):
    #     if row == self.rows or col == self.cols or self.matrix[row][col] == 0:
    #         return 0
        
    #     if (row, col) in self.cache:
    #         return self.cache[(row, col)]
        
    #     maxLength = 1 + min(
    #         self.dfs(row + 1, col),
    #         self.dfs(row, col + 1),
    #         self.dfs(row + 1, col + 1)
    #     )

    #     self.cache[(row, col)] = maxLength
    #     return maxLength