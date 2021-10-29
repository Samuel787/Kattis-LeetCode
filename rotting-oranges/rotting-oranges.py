class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # simulate the whole thing
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        rotten = set()
        fresh = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh.add((row, col))
                elif grid[row][col] == 2:
                    rotten.add((row, col))
        mins = 0
        while fresh:
            infected = set()
            for bad_orange in rotten:
                for direction in directions:
                    x = bad_orange[0] + direction[0]
                    y = bad_orange[1] + direction[1]
                    new_rotten = (x, y)
                    if new_rotten in fresh:
                        infected.add(new_rotten)
            if not infected:
                return -1
            
            for new_rotten in infected:
                rotten.add(new_rotten)
                fresh.remove(new_rotten)
            mins += 1
        return mins
          