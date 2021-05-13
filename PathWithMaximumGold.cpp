class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        if(grid.size() == 0 || grid[0].size() == 0){
            return 0;
        }
        int length = grid.size();
        int width = grid[0].size();
        int max_gold = 0;
        for(int i = 0; i < length; i++){
            for(int j = 0; j < width; j++){
                if(grid[i][j] > 0){
                    vector<vector<bool>> track;
                    for(int k = 0; k < length; k++){
                        vector<bool> sub_track;
                        for(int l = 0; l < width; l++){
                            sub_track.push_back(false);
                        }
                        track.push_back(sub_track);
                    }
                    int curr_gold = find_max_gold(grid, i, j, length, width, track);
                    max_gold = max(max_gold, curr_gold);
                }
            }
        }
        return max_gold;
    }
    
    int find_max_gold(vector<vector<int>>& map, int i, int j, int length, int width, vector<vector<bool>>& track){
        if(i < 0 || j < 0 || i >= length || j >= width || map[i][j] == 0 || track[i][j]){
            return 0;
        }
        int curr_gold = map[i][j];
        track[i][j] = true;
        int left = find_max_gold(map, i, j - 1, length, width, track);
        int right = find_max_gold(map, i, j + 1, length, width, track);
        int up = find_max_gold(map, i - 1, j, length, width, track);
        int down = find_max_gold(map, i + 1, j, length, width, track);
        curr_gold += max(max(left, right), max(up, down));
        track[i][j] = false;
        return curr_gold;
    }
};
