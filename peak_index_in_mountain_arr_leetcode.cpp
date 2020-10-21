class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        return helper(arr, 0, arr.size() - 1);    
    }
    
    int helper(vector<int> &arr, int left, int right){
        if(left == right){
            return left;
        }
        int mid = left + (right - left) / 2;
        if(arr[mid] < arr[mid + 1]){
            return helper(arr, mid + 1, right);
        } else {
            return helper(arr, left, right - 1);
        }
    }
};