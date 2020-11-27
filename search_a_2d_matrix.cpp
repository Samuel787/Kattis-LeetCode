class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        if(matrix.size() == 0 || matrix[0].size() == 0){
            return false;
        }
        
        int depth = matrix.size();
        int length = matrix[0].size();
        int up = 0;
        int down = depth -1;
        while(up <= down){
            int mid = (up + down) / 2;
            if(mid == 0 && matrix[mid][length - 1] >= target){
                    // binary search first row
                    return binary_search(matrix, mid, target);
                
            } else if(matrix[mid][length - 1] >= target && matrix[mid - 1][length - 1] < target){
                // binary search mid row
                return binary_search(matrix, mid, target);
            } else if(matrix[mid][length - 1] >= target){
                down = mid - 1;
            } else {
                up = mid + 1;
            }
        }
        return false;
    }
    
    bool binary_search(vector<vector<int>>& matrix, int row, int target){
        cout << row << endl;
        int start = 0;
        int end = matrix[0].size() -1;
        while(start <= end){
            int mid = (start + end) / 2;
            if(matrix[row][mid] == target){
                return true;
            } else if(matrix[row][mid] > target){
                end = mid - 1;
            } else if(matrix[row][mid] < target){
                start = mid + 1;
            }
        }
        return false;
    }
};