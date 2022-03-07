class Solution {
    
    
    public int findTargetSumWays(int[] nums, int target) {
    
        int maxSum = 0;
        for (int num: nums) {
            maxSum += num;
        }
        int minSum = -maxSum;
        int[][] dp = new int[nums.length][maxSum * 2 + 1];
        for (int i = 0; i < nums.length; i++) {
            int upperBound = maxSum * 2 + 1;
            for (int j = 0; j < upperBound; j++) {
                dp[i][j] = -1;
            }
        } 
        return backtrack(0, 0, minSum, nums, dp, target);
    }
    
    private int backtrack(int index, int sum, int minSum, int[] nums, int[][] dp, int target) {
        if (index == nums.length) {
            return (sum == target) ? 1 : 0;
        }
        if (dp[index][sum - minSum] != - 1) {
            return dp[index][sum - minSum];
        }
        dp[index][sum - minSum] = backtrack(index + 1, sum - nums[index], minSum, nums, dp, target) + backtrack(index + 1, sum + nums[index], minSum, nums, dp, target);
        return dp[index][sum - minSum];
    }
    
    
}