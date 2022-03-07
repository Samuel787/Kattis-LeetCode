class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        int[] dp = new int[days.length];
        for (int i = 0; i < days.length; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        return dfs(0, dp, costs, days);
    }
    
    public int dfs(int index, int[] dp, int[] costs, int[] days) {
        if (index == days.length) {
            return 0;
        }
        if (dp[index] != Integer.MAX_VALUE) {
            return dp[index];
        }
        int[] tix_opts = new int[]{1, 7, 30};
        for (int x = 0; x < 3; x++) {
            int d = tix_opts[x];
            int c = costs[x];
            int j = index;
            while (j < days.length && days[j] < days[index] + d) {
                j++;
            }
            dp[index] = Math.min(dp[index], c + dfs(j, dp, costs, days));
        }
        return dp[index];
    }
}