class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int height = matrix.size();
        if (height == 0) {
            return false;
        }
        int width = matrix[0].size();
        if (width == 0) {
            return false;
        }
        int col = width - 1;
        int row = 0;
        while (col >= 0 && row < height) {
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] > target) {
                col--;
            } else {
                row++;
            }
        }
        return false;
    }
};
