class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        if (poured == 0) {
            return 0;
        }
        List<Double> queue = new ArrayList<>();
        queue.add(Double.valueOf(poured));
        int curr_level = 0;
        while (query_row > curr_level) {
            List<Double> temp = new ArrayList<>();
            temp.add(Math.max(0, (queue.get(0) - 1) / 2));
            for (int i = 1; i < queue.size(); i++) {
                temp.add(Math.max(0, (queue.get(i - 1) - 1)/ 2) + Math.max(0, (queue.get(i) -1) / 2));
            }
            temp.add(Math.max(0, (queue.get(queue.size() - 1) - 1) / 2));
            queue = temp;
            curr_level++;
        }
        return Math.min(1, queue.get(query_glass));
    }
}