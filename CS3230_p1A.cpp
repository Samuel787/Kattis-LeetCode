#include <bits/stdc++.h>
using namespace std;

// dp array for memoization
int dp[700][50001];
int options[3] = {-1, 1, 0};

int generate_dp(int delta_rate, int curr_height, int initial_rate, int max_height, vector<bool> &isSacred){
    if(curr_height > max_height){
        return 0;
    }
    if(curr_height == max_height){
        if(isSacred[curr_height]){
            return 1;
        } else {
            return 0;
        }
    }
    if(dp[delta_rate][curr_height] != -1){
        return dp[delta_rate][curr_height];
    }

    if(isSacred[curr_height]){
        dp[delta_rate][curr_height] = 1;
    } else {
        dp[delta_rate][curr_height] = 0;
    }
    int curr_rate;
    if(delta_rate > 320){
        curr_rate = initial_rate - delta_rate + 320;
    } else {
        curr_rate = initial_rate + delta_rate;
    }

    for(int x : options){
        if(x == -1 && curr_rate <= 1){
            continue;
        } else {
            int new_rate = curr_rate + x;
            int new_delta_rate;
            if(new_rate < initial_rate){
                new_delta_rate = 320 + (initial_rate - new_rate);
            } else {
                new_delta_rate = new_rate - initial_rate;
            }
            if(curr_height + new_rate <= max_height){
                int dp_result = generate_dp(new_delta_rate, curr_height + new_rate, initial_rate, max_height, isSacred);
                if(isSacred[curr_height]){
                    dp_result++;
                }
                if(dp_result > dp[delta_rate][curr_height]){
                    dp[delta_rate][curr_height] = dp_result;
                }
            }
        }
    }

    return dp[delta_rate][curr_height];
}

int main(){
    int rorig, max_height;
    cin >> rorig;
    cin >> max_height;
    string sacred_string;
    cin >> sacred_string;
    vector<bool> isSacred;
    isSacred.push_back(false); //dummy
    for(int i = 0; i < sacred_string.size(); i++){
        if(sacred_string[i] == '.'){
            isSacred.push_back(false);
        } else if(sacred_string[i] == 's'){
            isSacred.push_back(true);
        }
    }
    for(int i = 0; i < 700; i++){
        for(int j = 0; j <= 50000; j++){
            dp[i][j] = -1;
        }
    }
    int result = generate_dp(0, 0, rorig, max_height, isSacred);
    cout << result << endl;
}