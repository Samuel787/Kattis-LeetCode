class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int result = 0;
        if (nums.size() < 3) {
            return result;
        }
        sort(nums.begin(), nums.end());
        for (int high = 2; high < nums.size(); high++) {
            int left = 0;
            int right = high - 1;
            while (left < right) {
                if (nums[left] + nums[right] > nums[high]) {
                    result += right - left;
                    right--;
                } else {
                    left++;
                }
            }
        }
        return result;
    }
};
