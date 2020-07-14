#include <bits/stdc++.h>
using namespace std;

bool containsNearbyDuplicate(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int start = 0;
        int end = nums.size()-1;
        while(start != end && start >= 0 && end < nums.size()){
            if(nums[end] - nums[start] == k){
                return true;
            } else if(nums[end] - nums[start] < k){
                end++;
            } else if(nums[end] - nums[start] > k){
                start++;
            }
        }
        return false;
}

int main(){
    vector<int> nums{0, 1, 2, 3, 4, 5};
    if(containsNearbyDuplicate(nums, 10)){
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
}