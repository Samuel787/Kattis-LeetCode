class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < nums2.length; i++) {
            while (!stack.empty() && stack.peek() < nums2[i]) {
                map.put(stack.pop(), nums2[i]);
            }
            stack.push(nums2[i]);
        }
        
        int[] results = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            results[i] = map.getOrDefault(nums1[i], -1);
        }
        return results;
    }
}