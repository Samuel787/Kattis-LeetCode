class Solution {
public:
    int arrangeCoins(int n) {
        long count = 0;
        int row = 0;
        while(count <= n){
            count += row + 1;
            if(count <= n){
                row++;
            }
        }
        return row;
    }
};