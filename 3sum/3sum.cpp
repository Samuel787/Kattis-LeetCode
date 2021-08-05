class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> results;
        if (nums.size() < 3) {
            return results;
        }
        for (int i = 0; i < nums.size() - 2; i++) {
            if (i == 0 || (i > 0 && nums[i] != nums[i-1])) {
                int sum = -nums[i];
                int low = i + 1;
                int high = nums.size() - 1;
                while (low < high) {
                    if (nums[low] + nums[high] == sum) {
                        vector<int> temp{nums[i], nums[low], nums[high]};
                        results.push_back(temp);
                        while (low < high && nums[low] == nums[low + 1]) {
                            low++;
                        }
                        while (high > low && nums[high] == nums[high - 1]) {
                            high--;
                        }
                        low++;
                        high--;
                    } else if (nums[low] + nums[high] > sum) {
                        high--;
                    } else {
                        low++;
                    }
                }
            }
        }
        return results;
    }
};