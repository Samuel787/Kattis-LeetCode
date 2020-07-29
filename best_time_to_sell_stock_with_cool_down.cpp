/**
 * dp[len][2]
 * case 1: We have the stock on day i, dp[i][1] max of the below:
 *   1.1. I bought it today
 *      1.1.2. dp[i-2][0] - prices[i]
 * 
 *   1.2. I'm carrying forward the stock
 *     1.2.1. dp[i-1][1] // same profit until i sell the stock
 * 
 * Case 2: We have no stock on day i, dp[i][0] max of the below:
 *   2.1. I sold it today
 *      2.1.1. dp[i-1][1] + prices[i]
 *   
 *   2.2. I am carrying forward, doing nothing
 *     2.2.1. dp[i-1][0]  //same profit until i do something
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int days = prices.size();
        if(days <= 1){
            return 0;
        }
        
        if(days == 2 && prices[1] > prices[0]){
            return prices[1] - prices[0];
        } else if(days == 2 && prices[0] >= prices[1]){
            return 0;
        }
        
        int dp[days][2];
        //vector<vector<int>> dp(days, vector<int> options(2)); // dynamic array to store the profits
        dp[0][0] = 0; //initially 0 if i dont buy
        dp[0][1] = -prices[0]; // i bought so i incur cost
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1]); // no stock on day 1 -> no stock on day 0 || sold on day 1
        dp[1][1] = max(dp[0][0]-prices[1], dp[0][1]); //stock on day 1 -> either bought today || carry forward from yesterday
        
        //construct the dynamic array
        for(int i = 2; i < days; i++){
            // no stock today -> no stock on day 0 || sold on day 1
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]);
            //stock on day 1 -> either bought today || carry forward from yesterday
            dp[i][1] = max(dp[i-2][0]-prices[i], dp[i-1][1]);
        }
        return dp[days - 1][0]; //must have sold the stock on the last day    
    }
};