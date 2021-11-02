class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = -1
        y = -1
        num_zeros = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x = i
                    y = j
                elif grid[i][j] == 0:
                    num_zeros += 1
        return self.dfs(grid, x, y, num_zeros)
        
    def dfs(self, grid, curr_x, curr_y, num_zeros):
        if curr_x < 0 or curr_y < 0 or curr_x >= len(grid) or curr_y >= len(grid[0]) or grid[curr_x][curr_y] == -1:
            return 0
        if grid[curr_x][curr_y] == 2:
            if num_zeros == -1:
                return 1
            return 0
        
        val = grid[curr_x][curr_y]
        grid[curr_x][curr_y] = -1
        num_zeros -= 1
        # perform dfs
        total = self.dfs(grid, curr_x + 1, curr_y, num_zeros)\
            + self.dfs(grid, curr_x - 1, curr_y, num_zeros)\
            + self.dfs(grid, curr_x, curr_y + 1, num_zeros)\
            + self.dfs(grid, curr_x, curr_y - 1, num_zeros)\
        
        grid[curr_x][curr_y] = val
        num_zeros += 1
        return total