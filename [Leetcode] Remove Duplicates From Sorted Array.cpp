class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        int begin = 0;
        for(int j = 1; j < nums.size(); j++){
            if(nums[begin] != nums[j]){
                nums[begin + 1] = nums[j];
                begin++;
            }
        }
        return begin + 1;
    }
};