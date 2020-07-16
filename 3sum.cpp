#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums){
    sort(nums.begin(), nums.end());
    vector<vector<int>> results;
    if(nums.size() < 3){
        return results;
    }
    for(int i = 0;  i < nums.size() -2; i++){
        if(i == 0 || nums[i] != nums[i-1]){
            //find two numbers that add up to the sum
            int sum = 0 - nums[i];
            int low = i + 1;
            int high = nums.size() - 1;
            while(low < high){
                //cout << "i: " << nums[i] << "first: " << nums[low] << "sec: " << nums[high] << "sum: " << sum << endl;
                vector<int> result; 
                if(nums[low] + nums[high] == sum){
                    //cout << "meow" << endl;
                    //found a solution
                    result.push_back(nums[i]);
                    result.push_back(nums[low]);
                    result.push_back(nums[high]);
                    results.push_back(result);
                    while(low < high && nums[low] == nums[low + 1]) low++;
                    while(low < high && nums[high] == nums[high - 1]) high--;
                    low++;
                    high--;
                } else if(nums[low] + nums[high] < sum){
                    low++;
                } else {
                    high--;
                }
            }
        }
    }
    return results;
}

// vector<vector<int>> threeSum(vector<int>& nums) {
   
//    vector<vector<int>> result;
//    if(nums.size() < 3){
//        return result;
//    }
//    sort(nums.begin(), nums.end());
//    map<int, int> data;
//    for(int i = 0; i < nums.size(); i++){
//        data.insert(pair<int, int>(nums[i], i));
//    }
//    for(int i = 0; i < nums.size() - 2; i++){
//         int initial = nums[i];
//         if(i == 0 || nums[i] != nums[i-1]){
//             for(int j = i+1; j < nums.size(); j++){
//                 if(j == i+1 || nums[j] != nums[j-1]){
//                     int complement = 0 - initial - nums[j];
//                     if(data.find(complement) != data.end() && j != data[complement]){
//                             vector<int> result1{nums[i], nums[j], complement};
//                             result.push_back(result1);
//                     }
//                 }
//             }
//         }
//     }
//     return result;
// }

/**
 * Driver code
 */
int main(){
    vector<int> initial{-1,0,1,0}; // -4, -1, -1, 0, 1, 2
    vector<vector<int>> soln = threeSum(initial);
    for(vector<int> res : soln){
        for(int i = 0; i < res.size(); i++){
            cout << res[i] << " ";
        }
        cout << endl;
    }
}