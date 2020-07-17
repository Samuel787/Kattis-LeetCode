/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    int longestUnivaluePath(TreeNode* root) {
        //if leaf node, return 0
        if(root -> left == nullptr && root -> right == nullptr){
            return 0;
        }
        int max_left, max_right;
        TreeNode* leftChild = root -> left;
        TreeNode* rightChild = root -> right;
        if(leftChild == nullptr){
            max_left = 0;
        } else if(leftChild -> val == root -> val){
            max_left = 1 + longestUnivaluePath(leftChild);
        } else {
            max_left = longestUnivaluePath(leftChild);
        }
        
        if(rightChild == nullptr){
            max_right = 0;
        } else if(rightChild -> val == root -> val){
            max_right = 1 + longestUnivaluePath(rightChild);
        } else {
            max_right = longestUnivaluePath(rightChild);
        }
        return max(max_left, max_right);
    }
};