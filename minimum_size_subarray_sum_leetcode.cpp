class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        int window_size = INT_MAX;
        int start_pointer = 0;
        int end_pointer = 0;
        int sum = nums[0];
        while(start_pointer < nums.size()){
            if(end_pointer == (nums.size() - 1) && sum < s){
                break;
            } else {
                if(sum >= s){
                    //check window size
                    int current_window = end_pointer - start_pointer + 1;
                    if(current_window < window_size){
                        window_size = current_window;
                    }
                    // try to drop something on the left
                    sum -= nums[start_pointer];
                    start_pointer++;
                } else {
                    // expand the right side
                    if(end_pointer == (nums.size() -1)){
                        // can't expand right anymore already
                        break;
                    } else {
                        end_pointer++;
                        sum += nums[end_pointer];
                    }
                }
            }
        }
        if(window_size == INT_MAX){
            return 0;
        } else {
            return window_size;
        }
    }
};