        int dp_result = generate_dp(new_delta_rate, curr_height + new_rate, initial_rate, max_height, isSacred);
        if(isSacred[curr_height]){
            dp_result++;
        }
        if(dp_result > dp[delta_rate][curr_height]){
            dp[delta_rate][curr_height] = dp_result;
        }