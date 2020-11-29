class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max1 = 0;
        int curr = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 1){
                curr+= 1;
                max1 = max(curr, max1);
            } else {
                curr = 0;
            }
        }
        return max1;
    }
};