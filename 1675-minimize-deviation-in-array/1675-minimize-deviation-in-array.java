class Solution {
    public int minimumDeviation(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->b-a);
        
        int min = Integer.MAX_VALUE;
        for (int i: nums) {
            if (i % 2 == 1) {
                i *= 2;
            }
            pq.add(i);
            if (i < min) {
                min = i;
            }
        }
        
        int diff = pq.peek() - min;
        while (pq.peek() % 2 == 0) {
            int top = pq.remove();
            top /= 2;
            min = Math.min(min, top);
            pq.add(top);
            diff = Math.min(diff, pq.peek() - min);
        }
        return diff;
    }
}