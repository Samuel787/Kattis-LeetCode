class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        if (nums.length < 3) {
            return 0;
        }
        int result = 0;
        int curr_diff = nums[1] - nums[0];
        int start = 0;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] - nums[i-1] != curr_diff) {
                result += getCount(start, i - 1);
                start = i - 1;
                curr_diff = nums[i] - nums[i - 1];
            }
        }
        result += getCount(start, nums.length - 1);
        return result;
    }
    
    private int getCount(int start, int end) {
        if (end - start < 2) {
            return 0;
        }
        int n = end - start - 1;
        if (n >= 0) {
            return n * (n + 1) / 2;
        } else {
            return 0;
        }
    }
}