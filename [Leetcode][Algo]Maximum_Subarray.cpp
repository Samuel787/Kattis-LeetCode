class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int start = 0;
        int end = 0;
        int running_sum = nums[0];
        int total_max = running_sum;
        for(int i = 1; i < nums.size(); i++){
            if(running_sum + nums[i] >= running_sum){
                running_sum += nums[i];
            } else {
                running_sum = nums[i];
            }
            total_max = max(total_max, running_sum);
            cout << "iteration: " << i << "running sum: " << running_sum << endl;
        }
        return total_max;
    }
};