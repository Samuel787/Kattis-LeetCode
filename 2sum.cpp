#include <bits/stdc++.h>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    map<int, int> data;
    for(int i = 0; i < nums.size(); i++){
        int complement = target - nums[i];
        if(data.find(complement) != data.end()){
            //we found a pair
            vector<int> result{data[complement], i};
            return result;
        }
        data.insert(pair<int, int>(nums[i], i));
    }
}

int main(){
    //driver for test inputs
    vector<int> input{2, 7, 11, 15};
    int target = 9;
    vector<int> result = twoSum(input, target);
    for(int i : result){
        cout << i << " ";
    }
    cout << endl;
}