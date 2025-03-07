class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = {}
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                if grid[col][row] in m:
                    m[grid[col][row]] += 1
                else:
                    m[grid[col][row]] = 1
        
        missing = -1
        repeated = -1
        for i in range(1, len(grid) * len(grid[0]) + 1, 1):
            if i not in m:
                missing = i
            if i in m and m[i] == 2:
                repeated = i
            if missing != -1 and repeated != -1:
                return [repeated, missing]
        return [-1, -1]