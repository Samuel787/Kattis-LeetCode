class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        if(nums.size() == 1){
            return nums[0];
        }
        
        // try O(n) solution
        int smallest = nums[0];
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] < smallest)
                smallest = nums[i];
        }
        return smallest;
    }
};