class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        self.rows = len(heights)
        self.cols = len(heights[0])
        self.heights = heights

        self.pacific = set()
        self.atlantic = set()

        for i in range(0, self.rows):
            self.dfs(i, 0, self.pacific, 0)
            self.dfs(i, self.cols - 1, self.atlantic, 0)

        for i in range(0, self.cols):
            self.dfs(0, i, self.pacific, 0)
            self.dfs(self.rows - 1, i, self.atlantic, 0)
        
        return list(self.pacific.intersection(self.atlantic))
        
    def dfs(self, row, col, visited, prevHeight):
        if (row < 0 or row >= self.rows or col < 0 or col >= self.cols) or (row, col) in visited or prevHeight > self.heights[row][col]:
            return

        visited.add((row, col))
        currHeight = self.heights[row][col]
        self.dfs(row + 1, col, visited, currHeight)
        self.dfs(row - 1, col, visited, currHeight)
        self.dfs(row, col + 1, visited, currHeight)
        self.dfs(row, col - 1, visited, currHeight)

        return 
        


        '''
        The approach below will not work for this case: [[0,2],[1,0],[1,1],[1,2],[2,0],[2,2]], 
        forcing us to use a DFS approach
        '''
    #     rows = len(heights)
    #     cols = len(heights[0])

    #     # first we find all sells that can go to pacific ocean. 
    #     terrain = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
    #     for i in range(cols):
    #         terrain[0][i][0] = 1
    #     for i in range(rows):
    #         terrain[i][0][0] = 1
        
    #     for i in range(1, rows):
    #         for j in range(1, cols):
    #             # check left
    #             if heights[i][j] >= heights[i][j - 1] and terrain[i][j - 1][0] == 1:
    #                 terrain[i][j][0] = 1
    #             elif heights[i][j] >= heights[i - 1][j] and terrain[i - 1][j][0] == 1:
    #                 terrain[i][j][0] = 1
                    
    #     # we find all cells that can go to atlantic ocean
    #     for i in range(cols):
    #         terrain[rows - 1][i][1] = 1
    #     for i in range(rows):
    #         terrain[i][cols - 1][1] = 1
        
    #     for i in range(rows - 2, -1, -1):
    #         for j in range(cols - 2, -1, - 1):
    #             if heights[i][j] >= heights[i][j + 1] and terrain[i][j + 1][1] == 1:
    #                 terrain[i][j][1] = 1
    #             elif heights[i][j] >= heights[i + 1][j] and terrain[i + 1][j][1] == 1:
    #                 terrain[i][j][1] = 1


    #     print("Heights: ")
    #     self.print_terrain(heights)
    #     print("Terrain: ")
    #     self.print_terrain(terrain)
    #     # we merge the results
    #     result = []
    #     for i in range(0, rows):
    #         for j in range(0, cols):
    #             if terrain[i][j][0] == 1 and terrain[i][j][1] == 1:
    #                 result.append([i, j])
        
    #     return result

    # def print_terrain(self, terrain):
    #     for i in range(len(terrain)):
    #         print(str(terrain[i]))




    #     self.rows = len(heights)
    #     self.cols = len(heights[0])
    #     self.heights = heights

    #     self.pacific = set()
    #     self.atlantic = set()

    #     # search from the cols
    #     for c in range(self.cols):
    #         self.dfs(c, 0, self.heights[0][c], self.pacific)
    #         self.dfs(c, self.rows -1, self.heights[self.rows - 1][c], self.atlantic)

    #     # search from the rows
    #     for r in range(self.rows):
    #         self.dfs(0, r, self.heights[r][0], self.pacific)
    #         self.dfs(self.cols - 1, r, self.heights[r][self.cols - 1], self.atlantic)

    #     result = []
    #     for key in self.pacific:
    #         if key in self.atlantic:
    #             result.append(key)

    #     return result

    # def dfs(self, x, y, prevHeight, visited):
    #     if (y, x) in visited or x < 0 or y < 0 or x >= self.cols or y >= self.rows or self.heights[y][x] < prevHeight:
    #         return
    #     visited.add((y, x))
    #     self.dfs(x, y + 1, self.heights[y][x], visited)
    #     self.dfs(x, y - 1, self.heights[y][x], visited)
    #     self.dfs(x + 1, y, self.heights[y][x], visited)
    #     self.dfs(x - 1, y, self.heights[y][x], visited)