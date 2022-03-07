class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        int pp = 1;
        int p = 2;
        int result = 2;
        for (int i = 3; i <= n; i++) {
            result = p + pp;
            pp = p;
            p = result;
        }
        return result;
    }
}