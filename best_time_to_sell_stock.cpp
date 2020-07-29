class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min = INT_MAX;
        int profit = 0;
        for(int i : prices){
            if(i < min){
                min = i; //no ones gonna sell at lowest price
            } else if(i - min > profit){
                profit = i - min; //sell off at a higher price than any previous possible profit point
            }
        }
        return profit;
    }
};