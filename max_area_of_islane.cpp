class Solution {
public:
    int max_area = 0;
    
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if(grid.size() == 0){
            return max_area;
        }
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == 1){
                    int curr_count = dfs(grid, i, j, 0);
                    max_area = max(max_area, curr_count);
                }
            }
        }
        return max_area;
    }
    
    int dfs(vector<vector<int>>& grid, int i, int j, int count){
        if(grid[i][j] == 1){
            grid[i][j] = 2;
            count += 1;
        }
        // check top
        if(i > 0 && grid[i - 1][j] == 1){
            count = dfs(grid, i - 1, j, count);
        }
        // check bottom
        if(i < grid.size() - 1 && grid[i + 1][j] == 1){
            count = dfs(grid, i + 1, j, count);
        }
        // check left
        if(j > 0 && grid[i][j - 1] == 1){
            count = dfs(grid, i, j - 1, count);
        }
        // check right
        if(j < grid[0].size() - 1 && grid[i][j + 1] == 1){
            count = dfs(grid, i, j + 1, count);
        }
        return count;
    }
};