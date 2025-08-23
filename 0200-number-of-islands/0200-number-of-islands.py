class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islandCount = 0
        self.grid = grid
        self.length = len(grid)
        self.width = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islandCount += 1
                    self.dfs(i, j)

        return islandCount

    def dfs(self, i, j):
        if i < 0 or i >= self.length:
            return
        if j < 0 or j >= self.width:
            return
        if self.grid[i][j] == 'x' or self.grid[i][j] == '0':
            return
        
        self.grid[i][j] = 'x'
        self.dfs(i - 1, j)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i, j + 1)

        
        
        