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
                    int curr_gold = find_max_gold(grid, i, j, length, width);
                    max_gold = max(max_gold, curr_gold);
                }
            }
        }
        return max_gold;
    }
    
    int find_max_gold(vector<vector<int>>& map, int i, int j, int length, int width){
        if(i < 0 || j < 0 || i >= length || j >= width || map[i][j] == 0 || map[i][j] == -1){
            return 0;
        }
        int curr_gold = map[i][j];
        map[i][j] = -1;
        int left = find_max_gold(map, i, j - 1, length, width);
        int right = find_max_gold(map, i, j + 1, length, width);
        int up = find_max_gold(map, i - 1, j, length, width);
        int down = find_max_gold(map, i + 1, j, length, width);
        map[i][j] = curr_gold;
        curr_gold += max(max(left, right), max(up, down));
        return curr_gold;
    }
};
