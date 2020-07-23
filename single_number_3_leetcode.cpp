class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        unordered_map<int, int> data;
        for(int i = 0; i < nums.size(); i++){
            data[nums[i]]++;
        }
        vector<int> result;
        for(auto x: data){
            if(x.second == 1)
                result.push_back(x.first);
        }
        return result;
    }
};