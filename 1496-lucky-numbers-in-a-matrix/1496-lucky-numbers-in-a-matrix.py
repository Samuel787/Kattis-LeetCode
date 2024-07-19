class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rowMins = set()
        colMins = [matrix[0][i] for i in range(len(matrix[0]))]
        for row in range(len(matrix)):
            minimum = matrix[row][0]
            for col in range(len(matrix[0])):
                if matrix[row][col] < minimum:
                    minimum = matrix[row][col]
                if matrix[row][col] > colMins[col]:
                    colMins[col] = matrix[row][col]
            rowMins.add(minimum)

        luckyNumbers = []
        for i in colMins:
            if i in rowMins:
                luckyNumbers.append(i)
        return luckyNumbers