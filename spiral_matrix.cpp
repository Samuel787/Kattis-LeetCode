class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> results;
        if(matrix.size() == 0){
            return results;
        }
        
        int leftTop = 0;
        int colStart = 0;
        int colEnd = matrix[0].size() - 1;
        int leftBottom = matrix.size() - 1;
        while(leftTop <= leftBottom && colStart <= colEnd){
            //print the first row
            for(int i = colStart; i <= colEnd; i++){
                results.push_back(matrix[leftTop][i]);
            }
            leftTop++;
            for(int i = leftTop; i <= leftBottom; i++){
                results.push_back(matrix[i][colEnd]);
            }
            colEnd--;
            //do a check for end
            // two cases:
            // cannot go back left if it has reached end
            // cannot go back up if has reached end
            if(leftTop > leftBottom || colStart > colEnd){
                break;   
            }
            for(int i = colEnd; i >= colStart; i--){
                results.push_back(matrix[leftBottom][i]);
            }
            leftBottom--;
            for(int i = leftBottom; i >= leftTop; i--){
                results.push_back(matrix[i][colStart]);
            }
            colStart++;
        }    
        return results;
    }
};