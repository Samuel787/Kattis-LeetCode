class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size() == 0 || matrix[0].size() == 0){
            return false;
        }
        
        int depth = matrix.size();
        int length = matrix[0].size();
        for(int i = 0; i < depth; i++){
            if(target <= matrix[i][length - 1]){
                for(int j = 0; j < length; j++){
                    if(matrix[i][j] == target){
                        return true;
                    }
                }
                return false;
            }
        }
        return false;
    }
};