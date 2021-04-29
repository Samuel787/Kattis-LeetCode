class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int running_max = nums[0];
        int current_max = running_max;
        for(int i = 1; i < nums.size(); i++){
            if(running_max + nums[i] >= nums[i]){
                running_max += nums[i];
            } else {
                running_max = nums[i];
            }
            current_max = max(current_max, running_max);
        }
        return current_max;
    }
};