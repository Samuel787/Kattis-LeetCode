class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> results;
        if(n==0){
            return results;
        }
        
        for(int i = 0; i < n; i++){
            vector<int> temp;
            for(int j = 0; j < n; j++){
                temp.push_back(-1);
            }
            results.push_back(temp);
        }
        
        int num = 1;
        int leftTop = 0;
        int leftBottom = n - 1;
        int colStart = 0;
        int colEnd = n - 1;
        n = n * n;
        while(num <= n){
            //go right first
            for(int i = colStart; i <= colEnd; i++){
                results[leftTop][i] = num;
                num++;
            }
            if(num > n) break;
            leftTop++;
            //go down
            for(int i = leftTop; i <= leftBottom; i++){
                results[i][colEnd] = num;
                num++;
            }
            if(num > n) break;
            colEnd--;
            
            //go left
            for(int i = colEnd; i >= colStart; i--){
                results[leftBottom][i] = num;
                num++;
            }
            if(num > n) break;
            leftBottom--;
            
            //go up
            for(int i = leftBottom; i >= leftTop; i--){
                results[i][colStart] = num;
                num++;
            }
            colStart++;
        }
        return results;
    }
};