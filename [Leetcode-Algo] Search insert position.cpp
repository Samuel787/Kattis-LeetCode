class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        while(start <= end){
            // cout << "start: " << start << " end: " << end << endl;
            if(target < nums[start]){
                if(start == 0){
                    return 0; // prepend to array
                } else {
                    if(target > nums[start - 1]){
                        return start;
                    } 
                    return start - 1;
                }
            } else if(target > nums[end]){
                return end + 1;
            }
            int mid = (start + end) / 2;
            if(nums[mid] == target){
                return mid;
            } else if(target < nums[mid]){
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return -1;
    }
};