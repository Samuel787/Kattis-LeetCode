#include <bits/stdc++.h>
using namespace std;

void print2d_vector(vector<vector<int>> arr){
    cout << "Printing the 2d vector" << endl;
    for(int i = 0; i < arr.size(); i++){
        for(int j = 0; j < arr[i].size(); j++){
            cout << arr[i][j] << " |";
        }
        cout << endl;
    }
    cout << endl;
}

int num_ways(vector<int> coins, int target){
    if(coins.size() == 0){
        return target == 0;
    }
    vector<vector<int>> dp;

    // bottom-up approach to building up the dp array
    for(int i = 0; i < coins.size(); i++){
        int currCoin = coins[i];
        vector<int> row;
        dp.push_back(row);
        for(int j = 0; j <= target; j++){
            if(j == 0){
                dp[i].push_back(1); // there is 1 way of forming 0 with no coins
            } else {
                if(currCoin > j){
                    if(i == 0){
                        dp[i].push_back(0); // there is no way
                    } else {
                        dp[i].push_back(dp[i-1][j]); // copy the value from the previous row cos can't use current coin
                    }
                } else {
                    if(i == 0){
                        // check if the value is divisible by current coin
                        if(j % currCoin == 0){
                            dp[i].push_back(1); // there is one way - using only such coins
                        } else {
                            dp[i].push_back(0); // no way
                        }
                    } else {
                        // 1. include coin
                        // 2. exclude coin
                        // 3. add 1 and 2
                        int include = dp[i][j - currCoin];
                        int exclude = dp[i - 1][j];
                        dp[i].push_back(include + exclude);
                    }
                }
            }
        }
    }

    //print2d_vector(dp);

    return dp[coins.size() - 1][target];
}

/**
 * Driver code
*/
int main(){
    vector<int> coins{1,2};

    cout << num_ways(coins, 2) << endl;
}