class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        unordered_map<int, int> nums2_index_mapping;
        for (int i = 0; i < nums2.size(); i++) {
            nums2_index_mapping[nums2[i]] = i;
        }
        
        for (int i = 0; i < nums1.size(); i++) {
            int cors_index = nums2_index_mapping[nums1[i]];
            bool found = false;
            for (int j = cors_index + 1; j < nums2.size(); j++) {
                if (nums2[j] > nums1[i]) {
                    found = true;
                    result.push_back(nums2[j]);
                    break;
                }
            }
            if (!found) {
                result.push_back(-1);
            }
        }
        return result;
        
        // vector<int> result;
        // sort(nums2.begin(), nums2.end());
        // for (int i = 0; i < nums1.size(); i++) {
        //     int index = binary_search(nums2, nums1[i]);
        //     bool added = false;
        //     for (int j = index + 1; j < nums2.size(); j++) {
        //         if (nums2[j] > nums1[i]) {
        //             result.push_back(nums2[j]);
        //             added = true;
        //             break;
        //         }
        //     }
        //     if (!added) {
        //         result.push_back(-1);
        //     }
        // }
        // return result;
    }
    
    // int binary_search(vector<int> arr, int target) {
    //     int low = 0;
    //     int high = arr.size() - 1;
    //     while (low < high) {
    //         int mid = (low + high) / 2;
    //         if (arr[mid] == target) {
    //             return mid;
    //         } else if (arr[mid] > target) {
    //             high = mid - 1;
    //         } else {
    //             low = mid + 1;
    //         }
    //     }
    //     return - 1;
    // }
};