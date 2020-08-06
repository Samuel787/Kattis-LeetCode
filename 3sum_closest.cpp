class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        
        int diff = INT_MAX;
        int result = 0;
        for(int i = 0; i < nums.size() - 2; i++){
            int left = i + 1;
            int right = nums.size() - 1;
            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                
                if(sum == target) return target;
                
                if(abs(sum - target) < diff){
                    diff = abs(target - sum);
                    result = sum;
                }
                
                if(sum < target){
                    left++;
                } else {
                    right--;
                }
            }
        }
        return result;
        
        
    }
};