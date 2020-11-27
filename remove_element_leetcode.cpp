class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int counter = 0;
        int start = 0;
        int end = nums.size() - 1;
        while(start <= end){
            if(nums[end] == val){
                end--;
                continue;
            } else if(nums[start] == val){
                swap(nums, start, end);
            } 
            start++;
            counter++;
        }

        return counter;
    }
    
    void swap(vector<int> &nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
};