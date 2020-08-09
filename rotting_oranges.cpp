class Solution {
public:
    
    /**
    Returns true if there is an update. False otherwise
    */
    bool updateBoard(vector<vector<int>>& grid){
        bool updated = false;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                if(grid[i][j] == 2){
                    //check up
                    if(i - 1 >= 0 && grid[i - 1][j] == 1){
                        grid[i - 1][j] = 3;
                    }
                    //check down
                    if(i + 1 < grid.size() && grid[i + 1][j] == 1){
                        grid[i + 1][j] = 3;
                    }
                    //check left
                    if(j - 1 >= 0 && grid[i][j - 1] == 1){
                        grid[i][j - 1] = 3;
                    }
                    //check down
                    if(j + 1 < grid[i].size() && grid[i][j + 1] == 1){
                        grid[i][j + 1] = 3;
                    }
                } 
            }
        }
        
        //change all the 3's to 1's
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                if(grid[i][j] == 3){
                    grid[i][j] = 2;
                    updated = true;
                    }
                }
            }
        
        return updated;
    }
    
    int orangesRotting(vector<vector<int>>& grid) {
        
        int timer = 0;
        while(updateBoard(grid)){
            //cout << timer << endl;
            timer++;
        }
        
        //check the board once
        bool all_rotten = true;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                if(grid[i][j] == 1){
                    all_rotten = false;
                }
            }
        }
        if(all_rotten){
            return timer;
        } else {
            return -1;
        }
    }
};