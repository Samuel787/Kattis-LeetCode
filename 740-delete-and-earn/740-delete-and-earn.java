class Solution {
    public int deleteAndEarn(int[] nums) {
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int num: nums) {
            if (countMap.containsKey(num)) {
                countMap.put(num, countMap.get(num) + 1);
            } else {
                countMap.put(num, 1);
            }
        }
        
        List<Integer> modifiedList = new ArrayList<>();
        for (Integer num: countMap.keySet()) {
            modifiedList.add(num);
        }
        Collections.sort(modifiedList);
        
        int res1 = 0;
        int res2 = 0;
        for (int i = 0; i < modifiedList.size(); i++) {
            if (i == 0) {
                res2 = modifiedList.get(i) * countMap.get(modifiedList.get(i));
            } else {
                if (modifiedList.get(i) == modifiedList.get(i - 1) + 1) {
                    int temp = Math.max(modifiedList.get(i) * countMap.get(modifiedList.get(i)) + res1, res2);
                    res1 = res2;
                    res2 = temp;
                } else {
                    res1 = res2;
                    res2 += modifiedList.get(i) * countMap.get(modifiedList.get(i));
                }
            }
        }
        return Math.max(res1, res2);
    }
}