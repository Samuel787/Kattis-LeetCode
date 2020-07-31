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
    TreeNode* invertTree(TreeNode* root) {
        if(root == nullptr){
            return nullptr;
        }
        
        TreeNode* left = root -> right;
        TreeNode* right = root -> left;
        if(left != nullptr){
            invertTree(left);
        }
        if(right != nullptr){
            invertTree(right);
        }
        
        root -> left = left;
        root -> right = right;
        
        return root;
    }
};