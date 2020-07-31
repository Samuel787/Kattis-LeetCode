class Solution {
public:

    
    int climb(int n, vector<int>& dp){
        if(dp[n] != -1){
            return dp[n];
        } else {
            dp[n-1] = climb(n-1, dp);
            dp[n-2] = climb(n-2, dp);
            return dp[n - 1] + dp[n - 2];
        }
    }
    
    int climbStairs(int n) {
        vector<int> dp(46, -1);
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        return climb(n, dp);
    }
};