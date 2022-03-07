class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int i = 1; i <= amount; i++) {
            dp[i] = 0; 
        }
        for (int coin : coins) {
            for (int i = 0; i <= amount; i++) {
                int remainder = i - coin;
                if (remainder >= 0) {
                    dp[i] += dp[remainder];
                }
            }
        }
        return dp[amount];
    }
}