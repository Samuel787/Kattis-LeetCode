#include <bits/stdc++.h>
using namespace std;

map<int, int> dp;

int calc_min(vector<int>& coins, int target, int num){
    if(target < 0){
        return -1; // invalid
    }
    if(target == 0){
        if(dp[target] > num){
            dp[target] = num;
        }
        return num;
    }
    if(dp.find(target) != dp.end()){
        return dp[target];
    }
    vector<int> results;
    int final_result = INT_MAX;
    for(int coin : coins){
        int result = calc_min(coins, target - coin, num + 1);
        cout << "The result is: " << result << endl;
        if(result > -1 && result <= final_result){
            final_result = result;
        }
    }
    dp[target] = final_result;
    return final_result;

}

/**
 * Driver code
*/
int main(){
    vector<int> coins{1, 5, 6, 9};
    int target = 11;
    cout << calc_min(coins, 11, 0);
}