class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        HashMap<Integer, Integer> mMap = new HashMap<>();
        for (int i = 0; i < tops.length; i++) {
            if (mMap.containsKey(tops[i])) {
                mMap.put(tops[i], mMap.get(tops[i]) + 1);
            } else {
                mMap.put(tops[i], 1);
            }
            if (mMap.containsKey(bottoms[i])) {
                mMap.put(bottoms[i], mMap.get(bottoms[i]) + 1);
            } else {
                mMap.put(bottoms[i], 1);
            }
        }
                
        int number = 0;
        for (Integer val: mMap.keySet()) {
            if (mMap.get(val) >= tops.length) {
                number = val;
                break;
            }
        }
        System.out.println(number);
        if (number == 0) {
            return -1;
        }
        
        int countOne = 0;
        int countTwo = 0;
        for (int i = 0; i < tops.length; i++) {
            if (tops[i] != number && bottoms[i] == number) {
                countOne++;
            } else if (tops[i] != number) {
                return -1;
            }
            if (bottoms[i] != number && tops[i] == number) {
                countTwo++;
            } else if (bottoms[i] != number) {
                return -1;
            }
        }
        return Math.min(countOne, countTwo);
        
        
                
    }
}