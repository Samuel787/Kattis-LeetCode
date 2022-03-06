class Solution {
    public int countOrders(int n) {
        long result = 1;
        int modulo = (int)Math.pow(10, 9) + 7;
        for (int i = 1; i <= n; i++) {
            result *= i;
            result %= modulo;
            result *= (2*i - 1);
            result %= modulo;
        }
        return (int)result;
    }
}