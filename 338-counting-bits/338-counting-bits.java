class Solution {
    public int[] countBits(int n) {
        int[] result = new int[n + 1];
        result[0] = 0;
        if (n == 0) {
            return result;
        }
        result[1] = 1;
        if (n == 1) {
            return result;
        }
        int currN = 2;
        while (currN <= n) {
            int temp = currN;
            for (int i = 0; i < temp && currN <= n; i++) {
                result[currN] = result[i] + 1;
                currN++;
            }            
        }
        return result;
    }
}