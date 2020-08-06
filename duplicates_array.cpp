class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> results;
        for(int i = 0; i < nums.size(); i++){
            int num;
            if(nums[i] > 0){
                num = nums[i];
            } else {
                num = -nums[i];
            }
            
            num--;
            if(nums[num] < 0){
                results.push_back(num + 1);
            } else {
                if(nums[num] > 0){
                    nums[num] *= -1;
                }
            }
        }
        return results;
    }
};