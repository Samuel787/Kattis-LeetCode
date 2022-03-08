/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return 0;
        }
        return pathSum(root.right, targetSum) + pathSum(root.left, targetSum) + pathSumInclude(root, targetSum);
    }
    
    private int pathSumInclude(TreeNode root, int targetSum) {
        int result = 0;
        if (root == null) {
            return result;
        }
        if (root.val == targetSum) {
            result += 1;
        }
        result += pathSumInclude(root.left, targetSum - root.val);
        result += pathSumInclude(root.right, targetSum - root.val);      
        return result;
    }
}