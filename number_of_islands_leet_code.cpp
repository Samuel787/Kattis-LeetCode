class Solution {
public:
    
    void print_grid(vector<vector<char>>& grid, int height, int width){
        for(int i = 0 ; i < height; i++){
            for(int j = 0; j < width; j++){
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
    
    int numIslands(vector<vector<char>>& grid) {
        int height = grid.size();
        if(height == 0){
            return 0;
        }
        int width = grid[0].size();
        if(width == 0){
            return 0;
        }
        //time to traverse the map
        int count = 0;
        for(int i=0; i < height; i++){
            for(int j=0; j < width; j++){
                if(grid[i][j] == '1'){
                    count++;
                    //print_grid(grid, height, width);
                    cout << endl;
                    stack<pair<int, int>> s;
                    s.push(make_pair(i, j));
                    while(!s.empty()){
                        pair<int, int> curr = s.top();
                        grid[curr.first][curr.second] = '2';
                        s.pop();
                        //check all its neighbours and push all 1's into stack
                        if(curr.first-1 >= 0){
                            if(grid[curr.first-1][curr.second] == '1'){
                                s.push(make_pair(curr.first-1, curr.second));
                            }
                        }
                        if(curr.first+1 < height){
                            if(grid[curr.first+1][curr.second] == '1'){
                                s.push(make_pair(curr.first+1, curr.second));
                            }
                        }
                        if(curr.second-1 >= 0){
                            if(grid[curr.first][curr.second-1] == '1'){
                                s.push(make_pair(curr.first, curr.second-1));
                            }
                        }
                        if(curr.second+1 < width){
                            if(grid[curr.first][curr.second+1] == '1'){
                                s.push(make_pair(curr.first, curr.second+1));
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
};