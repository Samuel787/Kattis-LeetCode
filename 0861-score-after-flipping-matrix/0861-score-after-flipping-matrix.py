class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # optimise horizontally first
        for i in range(0, len(grid), 1):
            currRow = grid[i]
            if currRow[0] == 0:
                for j in range(0, len(currRow), 1):
                    if currRow[j] == 0:
                        currRow[j] = 1
                    else:
                        currRow[j] = 0
            
        # optimise columns: if more 0s, flip the column
        totalCols = len(grid[0])
        totalRows = len(grid)
        for col in range(0, totalCols, 1):
            zeroCount = 0
            for row in range(0, totalRows, 1):
                if grid[row][col] == 0:
                    zeroCount += 1
            if totalRows - zeroCount * 2 < 0:
                # flip that column
                for row in range(0, totalRows, 1):
                    if grid[row][col] == 0:
                        grid[row][col] = 1
                    else:
                        grid[row][col] = 0
        
        # calculate the score
        totalScore = 0
        for row in grid:
            totalScore += self.calculateRow(row)
        return totalScore

                
    def calculateRow(self, row):
        power = 0
        total = 0
        for i in range(len(row) - 1, -1, -1):
            if (row[i] == 1):
                total += 2 ** power
            power += 1
        return total