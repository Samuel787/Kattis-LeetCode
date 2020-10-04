#include <bits/stdc++.h>
using namespace std;

int dp[700][50001];

int generate_dp(int delta_rate, int curr_height, int initial_rate, int max_height, vector<bool> &sacred_heights){
    if(curr_height > max_height){
        return 0;
    }
    if(curr_height == max_height){
        if(sacred_heights[max_height]){
            return 1;
        } else {
            return 0;
        }
    }
    if(dp[delta_rate][curr_height] != -1) {
        return dp[delta_rate][curr_height];
    }

    if(sacred_heights[curr_height]){
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
    
    if(curr_rate > 1){
        int new_rate = curr_rate - 1;
        int new_delta_rate ;
        if(new_rate < initial_rate){
            new_delta_rate = 320 + initial_rate - new_rate;
        } else {
            new_delta_rate = new_rate - initial_rate;
        }
        if(curr_height + new_rate <= max_height){
            if(sacred_heights[curr_height]){
                dp[delta_rate][curr_height] = max(dp[delta_rate][curr_height], generate_dp(new_delta_rate, curr_height + new_rate, initial_rate, max_height, sacred_heights) + 1);
            } else {
                dp[delta_rate][curr_height] = max(dp[delta_rate][curr_height], generate_dp(new_delta_rate, curr_height + new_rate, initial_rate, max_height, sacred_heights));
            }
        }
    }

    int new_rate = curr_rate + 1;
    int new_delta_rate;
    if(new_rate < initial_rate){
        new_delta_rate = 320 + initial_rate - new_rate;
    } else {
        new_delta_rate = new_rate - initial_rate;
    }
    if(curr_height + new_rate <= max_height){
        if(sacred_heights[curr_height]){
            dp[delta_rate][curr_height] = max(dp[delta_rate][curr_height], generate_dp(new_delta_rate, curr_height + new_rate, initial_rate, max_height, sacred_heights) + 1);
        } else {
            dp[delta_rate][curr_height] = max(dp[delta_rate][curr_height], generate_dp(new_delta_rate, curr_height + new_rate, initial_rate, max_height, sacred_heights));
        }
    }

    if(curr_height + curr_rate <= max_height){
        if(sacred_heights[curr_height]){
            dp[delta_rate][curr_height] = max(dp[delta_rate][curr_height], generate_dp(delta_rate, curr_height + curr_rate, initial_rate, max_height, sacred_heights) + 1);
        } else {
            dp[delta_rate][curr_height] = max(dp[delta_rate][curr_height], generate_dp(delta_rate, curr_height + curr_rate, initial_rate, max_height, sacred_heights));
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
    vector<bool> sacred_heights;
    sacred_heights.push_back(false);
    for(int i = 0; i < sacred_string.size(); i++){
        if(sacred_string[i] == 's'){
            sacred_heights.push_back(true);
        } else {
            sacred_heights.push_back(false);
        }
    }
    for(int i = 0; i < 700; i++){
        for(int j = 0; j <= 50000; j++){
            dp[i][j] = -1;
        }
    }
    cout << generate_dp(0,0, rorig, max_height, sacred_heights);
}