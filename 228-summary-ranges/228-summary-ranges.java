class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        if (nums.length == 0) {
            return result;
        }
        int leftIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                continue;
            }
            if (nums[i] == nums[i - 1] + 1) {
                continue;
            }
            // we have a breakage
            if (leftIndex == i - 1) {
                result.add(s(nums[leftIndex]));
            } else {
                result.add(s(nums[leftIndex]) + "->" + s(nums[i-1]));
            }
            leftIndex = i;
        }
        
        // account for the last guy
        if (leftIndex == nums.length - 1) {
            result.add(s(nums[leftIndex]));
        } else {
            result.add(s(nums[leftIndex]) + "->" + s(nums[nums.length - 1]));
        }
        return result;
    }
    
    public String s(int x) {
        return Integer.toString(x);
    }
}