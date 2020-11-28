class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int count = 0;
        if(grid.size() == 0){
            return count; 
        }
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == 1){
                    //check top
                    if(i == 0 || (i > 0 && grid[i - 1][j] == 0)){
                        count++;
                    } 
                    //check bottom
                    if(i == grid.size() - 1 || (i < grid.size() - 1 && grid[i + 1][j] == 0)){
                        count++;
                    }
                    //check left
                    if(j == 0 || (j > 0 && grid[i][j - 1] == 0)){
                        count++;
                    }
                    //check right
                    if(j == grid[0].size() - 1 || (j < grid[0].size() - 1 && grid[i][j + 1] == 0)){
                        count++;
                    }
                }
            }
        }
        return count;
    }
};