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

        # search from the cols
        for c in range(self.cols):
            self.dfs(c, 0, self.heights[0][c], self.pacific)
            self.dfs(c, self.rows -1, self.heights[self.rows - 1][c], self.atlantic)

        # search from the rows
        for r in range(self.rows):
            self.dfs(0, r, self.heights[r][0], self.pacific)
            self.dfs(self.cols - 1, r, self.heights[r][self.cols - 1], self.atlantic)

        result = []
        for key in self.pacific:
            if key in self.atlantic:
                result.append(key)

        return result

    def dfs(self, x, y, prevHeight, visited):
        if (y, x) in visited or x < 0 or y < 0 or x >= self.cols or y >= self.rows or self.heights[y][x] < prevHeight:
            return
        visited.add((y, x))
        self.dfs(x, y + 1, self.heights[y][x], visited)
        self.dfs(x, y - 1, self.heights[y][x], visited)
        self.dfs(x + 1, y, self.heights[y][x], visited)
        self.dfs(x - 1, y, self.heights[y][x], visited)