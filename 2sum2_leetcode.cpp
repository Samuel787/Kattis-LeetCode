class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int low = 0;
        int high = numbers.size() -1;
        vector<int> ans;
        while(low < high){
            if(numbers[low] + numbers[high] == target){
                ans.push_back(++low);
                ans.push_back(++high);
                break;
            } else if (numbers[low] + numbers[high] > target){
                while(numbers[high] == numbers[high -1]) high--;
                high--;
            } else {
                while(numbers[low] == numbers[low + 1]) low++;
                low++;
            }
        }
        return ans;
    }
};