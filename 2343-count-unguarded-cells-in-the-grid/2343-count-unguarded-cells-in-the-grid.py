class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        # put all the guards
        for r, c in guards:
            grid[r][c] = 2

        # put all the walls
        for r, c in walls:
            grid[r][c] = 2
        
        for r, c in guards:
            # scan right
            for i in range(c + 1, n):
                if grid[r][i] == 2:
                    break
                else:
                    grid[r][i] = 3
                
            # scan left
            for i in range(c - 1, -1, -1):
                if grid[r][i] == 2:
                    break
                else:
                    grid[r][i] = 3
            
            # scan up
            for i in range(r - 1, -1, -1):
                if grid[i][c] == 2:
                    break
                else:
                    grid[i][c] = 3
            
            # scan down
            for i in range(r + 1, m):
                if grid[i][c] == 2:
                    break
                else:
                    grid[i][c] = 3

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        return count